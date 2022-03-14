def solution(record):
    users = {}
    data = []
    for r in record:
        tmp = r.split()
        if tmp[0] == "Enter":
            users[tmp[1]] = tmp[2]
            data.append(f"{tmp[1]}님이 들어왔습니다.")
        elif tmp[0] == "Leave":
            data.append(f"{tmp[1]}님이 나갔습니다.")
        elif tmp[0] == "Change":
            users[tmp[1]] = tmp[2]
    for idx, d in enumerate(data):
        name = users[d[:d.index("님")]]
        data[idx] = name + d[d.index("님"):]
    return data