def solution(absolutes, signs):
    answer = 0
    for i, j in zip(absolutes, signs):
        if not j : i = -i
        answer += i
    return answer