def solution(n):
    k = list(str(int(n)))
    k.sort(reverse=True)
    return int(''.join(k))