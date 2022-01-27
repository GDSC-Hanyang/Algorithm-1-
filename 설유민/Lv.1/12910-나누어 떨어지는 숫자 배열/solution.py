def solution(arr, divisor):
    answer = sorted([n for n in arr if n / divisor == n // divisor])
    return answer if len(answer) > 0 else [-1]