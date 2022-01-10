# 완주하지 못한 선수
# 2022-01-10
# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]: return participant[i]
    return participant[-1]