def GCD(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def LCM(a, b):
    return abs(a * b) / GCD(a, b)

def solution(n, m):
    if n > m: n, m = m, n
    return [GCD(m, n), LCM(m, n)]