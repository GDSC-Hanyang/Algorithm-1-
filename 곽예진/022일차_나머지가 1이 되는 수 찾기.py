#나머지가 1이 되는 수 찾기
#https://programmers.co.kr/learn/courses/30/lessons/87389
#난이도 하

def solution(n):
    x=2
    while (n-1)%x != 0:
        x+=1
    answer = x
    return answer
