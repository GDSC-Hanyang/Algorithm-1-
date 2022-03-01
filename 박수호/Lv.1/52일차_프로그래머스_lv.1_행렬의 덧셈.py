def solution(arr1, arr2):
    n, m = len(arr1), len(arr1[0])
    answer = []
    for i in range(n):
        tmp = [0] * m
        for idx, a in enumerate(arr1[i]):
            tmp[idx] += a
        for idx, b in enumerate(arr2[i]):
            tmp[idx] += b
        answer.append(tmp)
    return answer