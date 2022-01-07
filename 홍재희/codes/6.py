# 없는 숫자 더하기
# 2022-01-06
# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    answer = sum(list({0, 1, 2, 3, 4, 5, 6, 7, 8, 9} - set(numbers)))
    return answer