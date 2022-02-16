def solution(n):
    answer = sorted(list(str(int(n))), reverse=True)
    return int("".join(answer))