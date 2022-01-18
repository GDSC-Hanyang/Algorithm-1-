# 폰켓못
# 2022-01-14
# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    typeN = len(set(nums))
    N = len(nums)
    if N/2 <= typeN:
        return N/2
    else:
        return typeN