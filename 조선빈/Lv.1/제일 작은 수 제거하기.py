def solution(arr):
    answer = []
    if len(arr) >= 2:
        arr.remove(min(arr))
        answer = arr
    else:
        answer.append(-1)
    return answer
