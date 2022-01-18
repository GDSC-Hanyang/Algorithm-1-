# 두 개 뽑아서 더하기
# 2022-01-19
# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                pass
            else:
                answer.add(numbers[i] + numbers[j])
    answer = list(answer)
    answer.sort()
    return answer