def solution(n):
    return min([i for i in range(2,n) if (n-1)%i==0])