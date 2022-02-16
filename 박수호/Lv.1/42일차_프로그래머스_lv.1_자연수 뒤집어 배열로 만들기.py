from collections import deque
def solution(n):
    answer = deque()
    n = str(n)
    for i in n:
        answer.appendleft(int(i))
    return list(answer)