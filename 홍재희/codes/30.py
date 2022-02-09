# 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = []
    key = {}
    for i in strings:
        if not(i[n] in key):
            key[i[n]] = [i]
        else:
            key[i[n]].append(i)
    for i in key.values():
        i.sort()
    keyIdx = list(key.keys())
    keyIdx.sort()
    for i in keyIdx:
        answer.extend(key[i])
    return answer
