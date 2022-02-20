def solution(n):
    for i in range(2,8000000):
        if n % pow(i,2) == 0:
            return pow(i+1,2)
        else:
            return -1
