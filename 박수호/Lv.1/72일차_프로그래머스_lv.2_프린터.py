from collections import deque
def solution(priorities, location):
    queue = deque(priorities)
    num = 0
    while queue:
        if queue[0] != max(queue):
            queue.append(queue.popleft())
        else:
            queue.popleft()
            num += 1
            if location == 0: break
        location = location - 1 if location else len(queue) - 1
    return num