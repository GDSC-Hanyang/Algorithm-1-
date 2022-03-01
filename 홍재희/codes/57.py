# 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    users = {}
    msg = {
        'Enter': '님이 들어왔습니다.',
        'Leave': '님이 나갔습니다.'
    }
    for i in record:
        data = i.split()
        if len(data) > 2:
            users[data[1]] = data[2]
    for j in record:
        data = j.split()
        if data[0] in msg:
            answer.append(users[data[1]] + msg[data[0]])
    return answer