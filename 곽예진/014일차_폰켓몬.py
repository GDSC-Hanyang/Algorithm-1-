#폰켓몬
#https://programmers.co.kr/learn/courses/30/lessons/1845
#난이도 중

def solution(nums):
    #원소 종류 개수 구하기
    nums.sort()
    count=1
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            count +=1
    #대소비교
    if count >= len(nums)/2 :
        answer=len(nums)/2
    else:
        answer=count
    
    return answer
