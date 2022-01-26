def solution(arr):
    return [arr[0]] + [arr[i] for i in range(1, len(arr)) if arr[i] != arr[i - 1]] 