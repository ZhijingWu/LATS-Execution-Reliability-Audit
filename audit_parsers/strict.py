"""Independent final-statement diagnostic. Never used by an agent or environment."""
import re

FLAGS = re.IGNORECASE | re.ASCII
FINAL = re.compile(r'Thus[ \t]+the[ \t]+correctness[ \t]+score[ \t]+is[ \t]+(10|[1-9])\.?', FLAGS)
LABEL = re.compile(r'\b(?:Thus[ \t]+the[ \t]+)?correctness[ \t]+score[ \t]+is[ \t]+([^\s]+)', FLAGS)
INTEGER = re.compile(r'(10|[1-9])\.?', re.ASCII)


def parse_final_score(text):
    """Return a score only for a valid final line with no conflicting labeled score.

    Whitespace at line edges, case differences and one trailing period are allowed.
    Markdown, quotes, signs, decimals, fractions, alternate labels and trailing prose
    are rejected. Earlier valid labeled scores that disagree cause abstention.
    Earlier malformed mentions are recorded; they never supply a replacement value.
    """
    if not isinstance(text, str):
        raise TypeError('diagnostic input must be text')
    lines = [line.strip(' \t\r') for line in text.split('\n') if line.strip(' \t\r')]
    mentions = []
    for match in LABEL.finditer(text):
        token = match.group(1)
        integer = INTEGER.fullmatch(token)
        mentions.append({'token': token, 'score': int(integer.group(1)) if integer else None,
                         'span': list(match.span())})
    result = {'status': None, 'score': None, 'normalized_value': None,
              'final_nonempty_line': lines[-1] if lines else None,
              'labeled_mentions': mentions, 'diagnostic_only': True,
              'decision_values_modified': False}
    final = FINAL.fullmatch(lines[-1]) if lines else None
    if final is None:
        if lines and re.search(r'correctness[ \t]+score', lines[-1], FLAGS):
            result['status'] = 'malformed_final_statement'
        elif any(m['score'] is not None for m in mentions):
            result['status'] = 'nonfinal_score_only'
        else:
            result['status'] = 'missing_final_score'
        return result
    score = int(final.group(1))
    if any(m['score'] is not None and m['score'] != score for m in mentions):
        result['status'] = 'conflicting_scores'
        return result
    result.update(status='accepted', score=score, normalized_value=score / 10)
    return result
