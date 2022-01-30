#내적
#https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    sum=0
    for i in range(len(a)):
         sum += a[i]*b[i]
    answer=sum
    return answer
