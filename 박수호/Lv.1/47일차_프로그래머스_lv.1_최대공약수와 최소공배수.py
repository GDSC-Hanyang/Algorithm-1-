def solution(n, m):
    a = max([i if n%i == 0 and m % i == 0 else -1 for i in range(1, min(n,m)+1)])
    b = n * m // a
    return [a, b]