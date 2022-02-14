# 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    try:
        int(s)
        return len(s) == 4 or len(s) ==6
    except:
        return False