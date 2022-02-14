# 문자열 내 p와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')