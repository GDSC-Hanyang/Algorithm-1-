from itertools import combinations

def isprime(num) :
    for n in range(2,int(pow(num,0.5))+1) :
        if num%n == 0 : return False
    return True

def solution(nums):
    return list(map(lambda combination : isprime(sum(combination)), combinations(nums, 3))).count(True)