# 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3

def solution(arr):
    answer = [arr[0]]
    for i in arr[1:]:
        if answer[-1] != i:
            answer.append(i)
    return answer