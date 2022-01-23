def solution(n, arr1, arr2):
    answer = [[0]*n for _ in range(n)]
    idx = 0
    for n1, n2 in zip(arr1, arr2):
        for i in range(n):
            answer[idx][n-1-i] = '#' if n1 % 2 or n2 % 2 else ' '
            n1, n2 = n1 // 2, n2 // 2
        answer[idx] = "".join(answer[idx])
        idx += 1
    return answer
