def solution(arr):
    before = -1
    answer = []
    for i in arr:
        if before == i:
            continue
        else:
            answer.append(i)
            before = i
    return answer