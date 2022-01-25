def solution(nums):
    answer = 0
    numList = []
    numsList = []
    #서로 다른 3개를 골라 더하기
    for i in range(0,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                numList.append(nums[i]+nums[j]+nums[k])
                numsList += [[i,j,k]]
   # print(numList)
   # print(numsList)
    #합들을 차례로 1부터 1000까지 나눠 나온 나머지가 0인 애들의 수를 센 후
    cntList = []
    for p in range(0,len(numList)):
        cnt = 0
        List = []
        for l in range(1,3001):
  # 수들이 최대 1000까지라고 했으므로 합은 3000까지,, 따라서 나누는 수가 3000까지 되어야 모두 판별할 수 있음
            if numList[p]%l == 0:
                cnt += 1
                List.append(l)
        if cnt == 2 :
            answer += 1
            a = numsList[p]
            b = numList[p]
            print(str(a)+'를 이용해서 '+str(b)+'를 만들 수 있습니다.')
        

    return answer
