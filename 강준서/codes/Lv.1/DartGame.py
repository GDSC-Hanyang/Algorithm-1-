def solution(dartResult):
    scores = []
    SDTidx = []
    ParsedResult = []

    for i, v in enumerate(dartResult):
        if v in "SDT": SDTidx.append(i)

    for i in range(3):
        if dartResult[SDTidx[i]+1 < len(dartResult) and SDTidx[i]+1] in "*#": SDTidx[i]+=1

        if i==0: ParsedResult.append(dartResult[0:SDTidx[i]+1])
        else: ParsedResult.append(dartResult[SDTidx[i-1]+1:SDTidx[i]+1])

    for i, v in enumerate(ParsedResult):
        temp = 0
        if v[1] == '0': 
            if v[2] == 'S': temp = 10
            elif v[2] == 'D': temp = 100
            else: temp = 1000

        else: 
            temp = int(v[0])
            if v[1] == 'D': temp = temp*temp
            elif v[1] == 'T': temp = temp*temp*temp

        scores.append(temp)

        if v[-1] == '*':
            scores[i]*=2
            if i!=0: scores[i-1]*=2
        elif v[-1] == '#': scores[i]*=(-1)

    return sum(scores)
  
