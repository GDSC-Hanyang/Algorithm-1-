from collections import Counter

def solution(N, stages):
    answer = []
    total = len(stages)
    C = sorted(Counter(stages).items())
    fail_ratio = {}

    # Calulate each fail_ratio
    for stage, cnt in C:
        fail_ratio[stage] = cnt/total
        total -= cnt
    if N+1 in stages : del fail_ratio[N+1]

    # if not in stages, it means fail ratio is 0.
    for i in range(1,N+1): 
        if i not in stages: fail_ratio[i]=0

    fail_ratio = sorted(fail_ratio.items(), key= lambda item: item[1], reverse = True)
    for i in fail_ratio : answer.append(i[0])

    return answer
