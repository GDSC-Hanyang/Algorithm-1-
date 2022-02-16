import re
def solution(s):
    answer = 0
    if '-' in s:
        s = re.sub('-','',s)
        answer = -int(s)
    else:
        s = re.sub('-','',s)
        answer = int(s)
    return answer
