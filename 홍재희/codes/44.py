# 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934

import math

def solution(n):
    if (n / int(math.sqrt(n))) == int(math.sqrt(n)):
        return (int(math.sqrt(n)) + 1) ** 2
    else:
        return -1