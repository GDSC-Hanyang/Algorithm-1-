#x만큼 간격이 있는 n개의 숫자
#https://programmers.co.kr/learn/courses/30/lessons/12954

#[1]번 풀이
def solution(x, n):
    answer = []
    for i in range(1,n+1):
        answer.append(x*i)
    return answer

#[2]번 풀이  
def solution(x, n):
    answer = [x*i for i in range(1,n+1)]
    return answer
