# 로또의 최고 순위와 최저 순위

import random

def solution(lottos, win_nums):
    i = j = 0
    sameCount = 0
    zeroCount = 0
    for i in range(0, 6):
        for j in range (0,6):  
            if lottos[i] == 0:
                zeroCount += 1
                break
            if lottos[i] == win_nums[j]:
                sameCount += 1
                break
                
    min = sameCount
    max = sameCount + zeroCount
    answer = [min, max]
    return answer



lottos = []
win_nums = []
i = j = 0
zeroCount = 0

for i in range(0,6):
    lot = random.randrange(0,45)
    if lot != 0:
        while lot in lottos:
            lot = random.randrange(0,45) 
    else:
        zeroCount += 1
    lottos.append(lot)
    i += 1
            
for j in range(0,6):
    win = random.randrange(1,45)
    while win in win_nums:
        win = random.randrange(1,45)  
    win_nums.append(win)
    j += 0
    
ans = solution(lottos, win_nums)
print("lottos\twin_nums\tresult")
print(lottos,"\t",win_nums)
print(ans)
    
        
    

