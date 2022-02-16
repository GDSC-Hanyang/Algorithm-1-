def solution(x, n):
    if x == 0:
        return [0 for i in range(0, n)]
    return [i if x > 0 else -i for i in range(abs(x), abs(x*n) + 1, abs(x))]