def solution(N, stages):
    answer = []
    for j in stages:
        if N<j:
            stages.remove(j)
            stages.append(N)
    stageA = list(set(stages))
    failP = []
    for i in range(0,len(stageA)):
        approach = 0
        for j in range(0,i+1):    
            approach += stages.count(stageA[j])
        not_clear = stages.count(stageA[i])
        if approach == 0:
            failP.append(0)
        else:
            failP.append(not_clear/approach)
    for i in range(0,len(stageA)):
        if len(failP) != 0:
            a = failP.index(max(failP))
            answer.append(stageA[a])
            del(stageA[a])
            failP.remove(max(failP))

    return answer
