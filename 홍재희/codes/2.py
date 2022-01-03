# 신규 아이디 추천
# 2022-01-02
# https://programmers.co.kr/learn/courses/30/lessons/72410

import re
def solution(new_id):
    answer = new_id.lower()
    p = re.compile('[a-z0-9\.\-\_]')
    answer = ''.join(p.findall(answer))
    while '..' in answer:
        answer = answer.replace('..', '.')
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    if answer == '':
        answer += 'a'
    if len(answer) >= 16:
        answer = answer[0:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) < 3:
        while len(answer) < 3:
            answer += answer[-1]
    return answer
