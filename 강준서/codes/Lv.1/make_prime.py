import itertools

def is_prime(n):
    if(n < 2): return False
    for i in range(2, n):
        if n % i == 0:
            return False 
    return True

def solution(nums):
    answer = 0
    cases = list(itertools.combinations((nums),3))
    for i in cases:
        if(is_prime(sum(i))):
            answer+=1

    return answer
