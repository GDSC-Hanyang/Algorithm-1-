from itertools import combinations
import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    nums.sort()
    for i in list(combinations(nums, 3)):
        tmp = sum(i)
        if isPrime(tmp):
            answer += 1
    return answer