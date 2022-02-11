def solution(n):
    fb = [0,1,1] #dp의 bottum up 방식을 활용함
    for i in range(3,n+1): fb.append((fb[i-2]+fb[i-1])%1234567)
    return fb[n]
