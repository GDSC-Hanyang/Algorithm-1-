def solution(dartResult):
    dR = list(dartResult)
    answer = []
    sult = []
    for i in range(len(dR)):
        if dR[i] == '1' and dR[i+1] == '0':
            sult.append('10')
        elif dR[i] =='0' and dR[i-1] == '1':
            continue
        else:
            sult.append(dR[i])

    for j in range(1,len(sult)):
        if sult[j] == "S":
            answer.append(int(sult[j-1]))
        elif sult[j] == "D":
            answer.append(int(sult[j-1])**2)
        elif sult[j] == "T":
            answer.append(int(sult[j-1])**3)

        if sult[j] == '*':
            if len(answer) >=2:
                answer[-1] = answer[-1]*2
                answer[-2] = answer[-2]*2
            else:
                answer[-1] = answer[-1]*2
        elif sult[j] == '#':
            answer[-1] = -answer[-1]
    answer = answer[0] + answer[1] + answer[2]
    
    return answer
