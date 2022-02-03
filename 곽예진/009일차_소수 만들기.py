#소수 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12977
#난이도 중상

def solution(nums):
    #임의의 세 수의 합 구하기
    sum=[]
    for i in range(len(nums)-2):
        for k in range(len(nums)-1):
            for r in range(len(nums)):
                if i<k and k<r:
                    sum.append(nums[i]+nums[k]+nums[r])
    print(sum)
    
    #소수리스트만들기_(1)자연수 리스트 만들기
    numlist=[] 
    num=1
    while num <= 3000 :
        numlist.append(num)
        num=num+1
    #소수리스트만들기_(2)합성수,1 제외하기
    
    q=1
    while q<=3000:
        for w in range(q): 
            if (w >= 2 and q % w == 0): #합성수 찾기
                numlist.remove(q)
                break
            if q==1:                     #1
                numlist.remove(q)
        q=q+1
            
    sosu=numlist        
    print(sosu)    
        
    #소수 개수 구하기
    count=0
    for l in sum:
        if l in sosu:
            count +=1
            
    return count
