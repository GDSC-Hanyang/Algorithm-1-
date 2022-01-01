def solution(record):
    recentNick = {}
    answer = []
    IDs = []
    
    for log in record:
        logs = log.split() #logs[0] = API, logs[1] = ID, logs[2] = Nickname
    
        if (logs[0]=='Enter') :
            answer.append("님이 들어왔습니다.")
            recentNick[logs[1]] = logs[2]
            IDs.append(logs[1])
            
        elif (logs[0]=='Leave') :
            answer.append("님이 나갔습니다.")
            IDs.append(logs[1])
            
        else :  #Change
            recentNick[logs[1]] = logs[2]
    
    for i, msg in enumerate(answer):
        answer[i] = recentNick[IDs[i]]+msg
    
    return answer
