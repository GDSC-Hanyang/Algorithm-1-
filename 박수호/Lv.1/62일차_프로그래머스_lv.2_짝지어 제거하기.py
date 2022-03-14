from collections import deque

def solution(s):
    s = deque(s)
    stack = []
    while s:
        a = s.popleft()
        if stack and stack[-1] == a:
            stack.pop()
        else:
            stack.append(a)

    return 0 if stack else 1