#문자열 내 p와 y의 개수
#https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    a=0
    b=0
    n=0
    for i in s:
        if i == 'p' or i =='P':
            a += 1
        if i == 'y' or i =='Y':
            b += 1
    if a==b:
        answer = True
    else:
        answer = False
    
    return answer
