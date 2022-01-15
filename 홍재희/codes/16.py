# 약수의 개수와 덧셈
# 2022-01-16
# https://programmers.co.kr/learn/courses/30/lessons/77884

def countDivisor(n):
    if n == 1:
        return False
    account = 2
    for i in range(2, n):
        if n % i == 0:
            account += 1
    return account % 2 == 0

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if countDivisor(i):
            answer += i
        else:
            answer -= i
    return answer