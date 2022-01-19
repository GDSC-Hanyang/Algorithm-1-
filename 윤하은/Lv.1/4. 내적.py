def solution(a, b):
    n = answer = 0
    while(n < len(a)):
        answer += a[n]*b[n]
        n += 1
    return answer