from collections import deque
def solution(s):
    pair = {'[':']',']':'x',
            '{':'}','}':'x',
            '(':')',')':'x'}
    answer = 0

    for start in range(len(s)):
        string = s[start:]+s[:start]
        stack = deque([])

        for char in string:
            if not stack or char!=pair[stack[0]]: stack.appendleft(char)
            else: stack.popleft()
        if not stack: answer+=1

    return answer
