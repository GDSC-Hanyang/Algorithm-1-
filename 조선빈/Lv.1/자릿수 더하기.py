def solution(n):
    n = str(n)
    answer = 0
    for i in range(len(n)):
        answer += int(n[i])
    return answer
