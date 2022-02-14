# 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    n, m = max(a, b), min(a, b)
    return ((n * (n + 1)) / 2) - ((m * (m - 1)) / 2)