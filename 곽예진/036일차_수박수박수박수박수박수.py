#수박수박수박수박수박수?
#https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    if n%2 ==0:
        answer="수박"*int(n/2)
    else:
        answer="수박"*int((n-1)/2)+"수"
    return answer
