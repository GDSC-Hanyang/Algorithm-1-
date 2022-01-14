# K번째 수
# 2021-01-11
# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for cmd in commands:
        x = array[(cmd[0] - 1):cmd[1]]
        x.sort()
        answer.append(x[cmd[2] - 1])
    return answer