# 숫자 문자열과 영단어
# 2022-01-03
# https://programmers.co.kr/learn/courses/30/lessons/81301


def solution(s):
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',  'eight', 'nine']
    for i, value in enumerate(num):
        if value in s: s = s.replace(value, str(i))
    answer = int(s)
    return answer