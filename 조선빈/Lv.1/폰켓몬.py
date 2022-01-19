def solution(nums):
    answer = 0
    numA = []
    for i in nums:
        if i not in numA:
            numA.append(i)
    if len(nums)//2 > len(numA):
        answer = len(numA)
    else:
        answer = len(nums)//2
    return answer
