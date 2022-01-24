def solution(s):
    return str(s[len(s) // 2]) if len(s) % 2 == 1 else str(s[len(s) // 2 - 1]) + str(s[len(s) // 2])