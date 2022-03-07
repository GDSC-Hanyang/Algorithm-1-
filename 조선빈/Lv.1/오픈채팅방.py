def solution(record):
    answer = []
    records = []
    dic = {}
    for i in range(len(record)):
        records.append(record[i].split(' '))
        if 'Enter' in records[i]:
            dic[records[i][1]] = records[i][2]
        if 'Change' in records[i]:
            dic[records[i][1]] = records[i][2]


    for i in range(len(records)):
        if 'Enter' in records[i]:
            answer.append(dic[records[i][1]]+'님이 들어왔습니다.')
        if 'Leave' in records[i]:
            answer.append(dic[records[i][1]]+'님이 나갔습니다.')
    return answer
