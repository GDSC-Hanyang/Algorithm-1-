from collections import Counter
def solution(nums):
    C = Counter(nums)
    return min(len(C),len(nums)//2)
  
