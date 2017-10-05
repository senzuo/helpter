import re

def getTag(s):
    pattern = re.compile(r'\【.*\】|\[.*\]')
    tags = re.findall(pattern,s)
    result = ''
    for tag in tags:
        result += tag +' '
    if len(result) < 2:
        return '-'
    return result