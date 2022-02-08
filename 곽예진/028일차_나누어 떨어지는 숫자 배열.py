#나누어 떨어지는 숫자 배열
#https://programmers.co.kr/learn/courses/30/lessons/12910
#난이도 중하

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor==0:
            answer.append(i)
    if len(answer)==0:
        answer=[-1]
    answer.sort()
    return answer
