from collections import deque

def solution(s):
    L = deque(list(s))
    stack = deque([L.popleft()])

    while L:
        if not stack or stack[-1] != L[0]: stack.append(L.popleft())
        else: 
            stack.pop()
            L.popleft()

    return 0 if stack else 1
  
