def solution(numbers):
    all = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    answer = sum(all - set(numbers))
    return answer
