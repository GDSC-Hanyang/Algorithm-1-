def solution(x):
    return x % sum([int(n) for n in list(str(x))]) == 0