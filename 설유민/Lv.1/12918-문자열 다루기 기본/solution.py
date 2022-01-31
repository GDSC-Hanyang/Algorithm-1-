import re
def solution(s):
    return (len(s) == 4 or len(s) == 6) and re.fullmatch(r'\d+', s) != None