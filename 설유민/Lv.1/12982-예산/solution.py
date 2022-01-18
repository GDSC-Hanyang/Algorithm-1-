def solution(d, budget):
    answer = 0
    d = sorted(d)
    for dept in d:
        if dept > budget:
            break
        budget -= dept
        answer += 1
    return answer