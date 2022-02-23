# 정수 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    return int(''.join(sorted(list(str(int(n))), reverse=True)))

print(solution(9128374.0))