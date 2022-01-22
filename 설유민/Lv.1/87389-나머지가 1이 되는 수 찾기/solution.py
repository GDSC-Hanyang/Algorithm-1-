from math import sqrt
def solution(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 1:
            return i
    return n - 1