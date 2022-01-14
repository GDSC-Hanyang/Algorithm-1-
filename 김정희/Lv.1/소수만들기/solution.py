from itertools import combinations

def isPrime(num):
    for i in range(2, int(num / 2)): #int(num**0.5가 더 바람직) !!
        if (num % i) == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for i in list(combinations(nums, 3)):
        if isPrime(sum(i)):
            answer += 1
    return answer