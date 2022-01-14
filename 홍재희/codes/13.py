# 체육복
# 2022-01-13
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    c0 = list(set(lost) - (set(lost) & set(reserve)))
    c2 = list(set(reserve) - (set(lost) & set(reserve)))
    answer = n - len(c0)
    for i in c0:
        for j in c2:
            if abs(i - j) == 1:
                answer += 1
                c2.remove(j)
                break
    return answer