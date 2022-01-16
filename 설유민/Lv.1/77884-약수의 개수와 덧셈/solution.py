def solution(left, right):
    answer = 0
    square = [num**2 for num in range(1, 32)]
    for num in range(left, right + 1):
        if num not in square:
            answer += num
        else:
            answer -= num
    return answer