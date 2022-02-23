# 나머지가 1이 되는 수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    answer = 0
    for i in range(2, n):
        if (n - 1) % i == 0:
            answer = i
            break
    return answer