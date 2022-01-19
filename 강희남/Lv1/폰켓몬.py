def solution(nums): #[3,1,2,3]
    list = []
    for num in nums :
        if len(list) == len(nums)/2 : break
        if num not in list :
            list.append(num)
    return len(list)