#두 정수 사이의 합
#https://programmers.co.kr/learn/courses/30/lessons/12912
#난이도 하

def solution(a, b):
    answer = 0
    ai=a
    bi=b
    if ai>bi:
        a=bi
        b=ai
    if a==b:
        answer=a
    else:
        for i in range(a,b+1):
            answer += i
    
    return answer
