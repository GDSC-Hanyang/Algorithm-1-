def solution(x, n): return list(range(x,x*n+int(x/abs(x)),x)) if (x!=0) else [0]*n
