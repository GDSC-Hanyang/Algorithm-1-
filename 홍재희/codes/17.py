# 3진법 뒤집기
# 2022-01-17
# https://programmers.co.kr/learn/courses/30/lessons/68935

import math

def solution(n):
    result = ''
    while n > 0:
        result += str(n % 3)
        n = math.floor(n / 3)
    answer = int(result, 3)
    return answer