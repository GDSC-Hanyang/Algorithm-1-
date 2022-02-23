from itertools import permutations

def solution(numbers):
    # 소수 찾기 알고리즘
    def IsPrime(n):
        if n==1 or n==0: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: return False
        return True

    nums = []
    for i in range(1,len(numbers)+1):
        for i in set(permutations(numbers,i)):
            temp = int(''.join(i))
            if IsPrime(temp): nums.append(temp)

    return len(set(nums))
