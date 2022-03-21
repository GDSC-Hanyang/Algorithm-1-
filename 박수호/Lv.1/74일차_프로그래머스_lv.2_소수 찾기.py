from itertools import permutations

def isPrime(num):
    if num == 1 or num == 0: return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    data = set()
    for i in range(1, len(numbers)+1):
        a = list(permutations(numbers, i))
        for j in a:
            b = int("".join(j))
            data.add(b)
    data = list(data)
    answer = 0
    for i in data:
        if isPrime(i):
            answer += 1
    return answer