from collections import deque

def solution(dartResult):
    
    stack = deque()
    score = ''
    answer = 0
    
    for i in range(len(dartResult)) :
        if dartResult[i].isdigit() :
            score += dartResult[i]
            
        elif dartResult[i] == 'S' :
            stack.append(int(score)**1)
            score = ''
            
        elif dartResult[i] == 'D' :
            stack.append(int(score)**2)
            score = ''

        elif dartResult[i] == 'T' :
            stack.append(int(score)**3)
            score = ''
        
        elif dartResult[i] == '*' :
            a = 2 * stack.pop()
            if stack :
                b = 2 * stack.pop()
                stack.append(b)
            stack.append(a)

        elif dartResult[i] == '#' :
            stack.append((-1) * stack.pop())
    
    while (stack):
        answer += stack.pop()

    return answer