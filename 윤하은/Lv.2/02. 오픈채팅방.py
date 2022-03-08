def solution(record):

    chatName = {}
    result = []
    temp = []

    for i in range(len(record)) :
        # [0] = Enter / Change / Leave, [1] = userID, [2] = name
        temp.append(record[i].split(' '))
        if temp[i][0] != 'Leave':
            chatName[temp[i][1]] = temp[i][2]

    for j in range(len(temp)) :
        if 'Enter' in temp[j]:
            result.append(chatName[temp[j][1]] + '님이 들어왔습니다.')
        if 'Leave' in temp[j]:
            result.append(chatName[temp[j][1]] + '님이 나갔습니다.')

    return result