# 실패율
# 2022-01-15
# https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    answer = []
    ratioList = []
    for i in range(N):
        onStage = stages.count(i+1)
        clearStage = len(list(filter(lambda x: x > i, stages)))
        if clearStage == 0:
            ratioList.append([0, N - (i + 1)])
        else:
            failRatio = onStage / clearStage
            ratioList.append([failRatio, N - (i + 1)])
    ratioList.sort(reverse=True)
    for i in ratioList:
        answer.append(N - i[1])
    return answer