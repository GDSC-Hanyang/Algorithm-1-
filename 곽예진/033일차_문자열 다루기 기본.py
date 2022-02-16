#문자열 다루기 기본
#https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    if len(s) != 4 and len(s) != 6:
        answer= False
    else:
        answer=s.isdecimal()
    return answer
