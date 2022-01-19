def solution(n, m):
    mul = n*m
    while m: n,m=m,n%m
    return [n,mul/n]
