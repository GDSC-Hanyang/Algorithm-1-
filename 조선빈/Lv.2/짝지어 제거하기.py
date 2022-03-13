def solution(s):
    answer = 0
    s = list(s)
    stack = []
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
    if len(stack) != 0:
        answer = 0
    else:
        answer = 1
    return answer
