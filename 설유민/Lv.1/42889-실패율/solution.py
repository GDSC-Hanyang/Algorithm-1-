def solution(N, stages):
    answer = []
    fail = [0 for i in range(0, N + 1)]
    clear = [0 for i in range(0, N + 1)]
    rate = [0 for i in range(0, N)]
    for stage in stages:
        for prev_stage in range(0, stage - 1):
            clear[prev_stage] += 1
        fail[stage - 1] += 1
    for i in range(0, N):
        if (fail[i] + clear[i]) == 0:
            rate[i] = 0
        else:
            rate[i] = fail[i] / (fail[i] + clear[i])
    for i in range(0, N):
        answer.append(rate.index(max(rate)) + 1)
        rate[rate.index(max(rate))] = -1
    return answer