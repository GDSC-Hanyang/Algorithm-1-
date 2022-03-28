def solution(s):
    answer = 0
    left_brackets = ['(', '{', '[']
    right_brackets = [')', '}', ']']
    for i in range(0, len(s)):
        rotated_s = (s + s)[i:i+len(s)]
        stack = []
        balanced = True
        for c in rotated_s:
            if c in left_brackets:
                stack.append(c)
            elif c in right_brackets:
                if len(stack) == 0:
                    balanced = False
                    break
                if stack[-1] == left_brackets[right_brackets.index(c)]:
                    stack.pop()
                else:
                    balanced = False
                    break
        if len(stack) == 0 and balanced:
            answer += 1
    return answer