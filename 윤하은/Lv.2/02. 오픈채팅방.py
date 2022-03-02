def solution(record):
    
    chatName = {}
    resultTemp = []
    result = []
    
    for i in range(len(record)) :
        # [0] = Enter / Change / Leave, [1] = userID, [2] = name
        temp = record[i].split(' ') 
        
        if temp[0] == 'Enter':
            chatName.setdefault(temp[1])
            chatName[temp[1]] = temp[2]
            new = temp[1] + '님이 들어왔습니다'
            resultTemp.append(new)
            
        elif temp[0] == 'Leave':
            new = temp[1] + '님이 나갔습니다.'
            del chatName[temp[1]]
            resultTemp.append(new)
            
        elif temp[0] == 'Change':
            chatName.pop(temp[1])
            chatName.setdefault(temp[1])
            chatName[temp[1]] = temp[2]
        
    for j in resultTemp :
        for uid, name in chatName.items() :
            if j[:-9] == uid :
                answer = j.replace(uid, name)
            #if answer[:-9] == uid :
                if '.' not in answer :
                    answer += '.'
                result.append(answer)
                break
        
    return result