# 약수의 합
# https://programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    if n == 0: return 0
    i = 2
    answer = {1, n}
    while i <= (n / 2):
        if n % i == 0:
            answer = answer | {i, n / i}
        i += 1
    return sum(answer)