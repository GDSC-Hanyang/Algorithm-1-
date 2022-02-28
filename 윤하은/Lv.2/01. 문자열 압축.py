from collections import deque

def solution(s):
    temp = 0
    stackValue = 0
    sorryList = [] 
    stack = deque()
    check = False

    for i in range(1, len(s) // 2 + 1):
        check = True
        length = i

        tList = [s[k:k+length] for k in range(0, len(s), length)]

        bar = tList[0]
        for j in range(0, len(tList)):
            if bar == tList[j]: temp += 1
                
            else : 
                bar = tList[j]
                stack.append(temp)
                temp = 1
        stack.append(temp)

        while (stack) :
            tmpStack = stack.popleft()
            if tmpStack > 1 :
                stackValue = stackValue + len(str(tmpStack)) + i
            else : 
                if stack : stackValue += i
                else :
                    tmpTlist = tList[len(tList)-1]
                    stackValue += len(tmpTlist)

        sorryList.append(stackValue)
        stackValue = 0
        temp = 0

    if check != True : return 1
    else : return min(sorryList)