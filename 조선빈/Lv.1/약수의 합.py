def solution(n):
    answer = 0
    s = []
    for i in range(1,n+1):
        if n % i == 0:
            s.append(i)
    answer = sum(s)
    return answer
