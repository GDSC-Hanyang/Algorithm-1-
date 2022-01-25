def solution(d, budget):
    answer = 0
    arrayD = sorted(d)
    cnt = 0
    for i in arrayD:
        if answer+i<=budget:
            answer = answer+i
            cnt += 1
        else:
            answer = answer
            break
    return cnt
