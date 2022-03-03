# 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    r = ['1', '2', '4']
    arr = []
    n -= 1
    while n > 2:
        arr.append(r[n % 3])
        n = (n // 3) - 1
    arr.append(r[n % 3])
    return ''.join(reversed(arr))