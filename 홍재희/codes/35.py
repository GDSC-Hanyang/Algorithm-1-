# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    arr = [False, False] + [True for i in range(2, n + 1)]
    for i in range(2, n + 1):
        if arr[i] == True:
            j = i * 2
            while j <= n:
                arr[j] = False
                j += i
    return arr.count(True)