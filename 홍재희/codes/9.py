# 소수 만들기
# 2022-01-09
# https://programmers.co.kr/learn/courses/30/lessons/12977

import math
def isPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def solution(nums):
    answer = 0
    x = 1
    y = 2
    for i in nums:
        for j in nums[x:]:
            for k in nums[y:]:
                if isPrime(i+j+k):
                    answer += 1
                    print(i, j, k, i+j+k)
            y += 1
        x += 1
        y = x + 1
    return answer