def solution(x, n):
    answer = []
    cnt = 0
    add = x
    while cnt<n:
        answer.append(add)
        add = x + add
        cnt += 1
    return answer
