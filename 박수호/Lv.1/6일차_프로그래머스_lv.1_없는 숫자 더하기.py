def solution(numbers):
    answer = 0
    numbers = set(numbers)
    diff = set([0,1,2,3,4,5,6,7,8,9]) - numbers
    for i in diff:
        answer += 1
    return answer