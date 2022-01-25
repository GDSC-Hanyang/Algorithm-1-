# 모의고사
# 2022-01-12
# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    score = [0, 0, 0]
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, value in enumerate(answers):
        if p1[i % 5] == value:
            score[0] += 1
        if p2[i % 8] == value:
            score[1] += 1
        if p3[i % 10] == value:
            score[2] += 1
    if max(score) == score[0]:
        answer.append(1)
    if max(score) == score[1]:
        answer.append(2)
    if max(score) == score[2]:
        answer.append(3)
    return answer