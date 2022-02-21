from itertools import permutations
from math import factorial, sqrt
def solution(numbers):
    numbers = list(numbers)
    permutation = set([int(''.join(element)) for length in range(1, factorial(len(numbers)) + 1) for element in permutations(numbers, length)])
    try:
        permutation.remove(0)
    except:
        pass
    try:
        permutation.remove(1)
    except:
        pass
    answer = 0
    for element in permutation:
        for number in range(2, int(sqrt(element)) + 1):
            if element % number == 0:
                break
        else:
            answer += 1
    return answer