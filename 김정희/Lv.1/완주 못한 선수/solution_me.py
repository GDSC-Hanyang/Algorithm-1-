def solution(participant, completion):
    a = list(set(participant) - set(completion))  # set을 하면 자동으로 중복이 제거된다
    if a == []:
        for x in participant:
            y = participant.count(x)
            if y > 1 and y > completion.count(x):  # and를 써서 불필요한 작업을 없앤다
                return x
    else:
        return a[0]

# 정렬하고 요소 비교해서 달라질 때 답내는 방법도 아주 굿 !!! 멍청이이