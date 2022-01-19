import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 객체는 빼기가 가능하다 ! 딕셔너리 형태로 만들어서 뺀다 !~!~!~!~!~ 천재임