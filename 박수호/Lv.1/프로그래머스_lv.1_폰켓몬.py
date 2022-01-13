from collections import Counter

def solution(nums):
    return len(Counter(nums)) if len(nums)//2 >= len(Counter(nums)) else len(nums)//2