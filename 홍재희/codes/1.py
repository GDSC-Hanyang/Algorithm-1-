# 로또의 최고 순위와 최저 순위
# 2022-01-01
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    minCount = len(set(lottos) & set(win_nums))
    maxCount = minCount + lottos.count(0)
    if (7 - minCount) < 7:
        return [7 - maxCount, 7 - minCount]
    elif (7 - maxCount) < 7:
        return [7 - maxCount, 6]
    else:
        return [6, 6]