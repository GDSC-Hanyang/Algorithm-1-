def solution(d, budget):
    d.sort()
    answer = 0
    for i in range(len(d)):
        budget -= d[i]
        if budget < 0: break
        answer += 1
    return answer