def solution(N, stages):
    tmp = dict()
    for i in range(N+1):
        tmp[i] = stages.count(i)
    fail = dict()
    cnt = 0
    for i in range(1, N+1):
        cnt += stages.count(i-1)
        fail[i] = tmp[i]/(len(stages)-cnt) if cnt != len(stages) else 0.0
    answer = [keys for keys, value in sorted(fail.items(), reverse=True, key = lambda item:item[1])]
    print(answer)
    return answer