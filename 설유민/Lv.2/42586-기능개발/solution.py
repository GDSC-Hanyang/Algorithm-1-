from math import ceil
def solution(progresses, speeds):
    answer = []
    times = [ceil((100 - progresses[i]) / speeds[i]) for i in range(0, len(speeds))]
    max = 0
    for t in times:
        if t > max:
            max = t
            answer.append(1)
        else:
            answer[-1] += 1
    return answer