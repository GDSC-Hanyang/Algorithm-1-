def solution(arr): 
    nums = ''
    ans = []

    for i in arr: nums+=str(i)

    for i in range(10):
        target = str(i)+str(i)
        while target in nums:
            nums = nums.replace(target,str(i))

    for i in nums: ans.append(int(i))

    return ans
  
