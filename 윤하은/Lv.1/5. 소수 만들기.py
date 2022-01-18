#소수만들기

import itertools

#부분합이 소수인지 판별 -> 인자 : 부분합
def isPrime(sumPrime):
    for i in range(2, sumPrime):
        if (sumPrime % i == 0):
            return False
    return True

#nums에서 원소 세 개를 뽑아 길이가 3 조합을 만들고 그 부분합을 isPrime 인자로
def solution(nums):
    j = answer = 0
    numsThr = list(itertools.combinations(nums, 3))
    while (j < len(numsThr)):
        sP = sum((list(numsThr[j])))
        if (isPrime(sP) == True):
            print(str(numsThr[j]) + '를 이용해서 '+ str(sP) + '을 만들 수 있습니다.')
            answer += 1
        j += 1
    return answer