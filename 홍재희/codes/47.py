# 최대공약수와 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    maxDivisior = 1
    minMultiple = m
    for i in range(2, min(n, m) + 1):
        if (n % i) == 0 and m % i == 0: maxDivisior = i
    j = 1
    while (max(n, m) * j) % min(n, m) != 0:
        j += 1
    minMultiple = max(n, m) * j
    return [maxDivisior, minMultiple]