def solution(record):
    result = []
    members = dict()
    for r in record:
        info = r.split(' ')
        if info[0] == "Enter" or info[0] == "Change":
            members[info[1]] = info[2]
    for r in record:
        if "Enter" in r:
            result.append(f"{members[r.split(' ')[1]]}님이 들어왔습니다.")
        elif "Leave" in r:
            result.append(f"{members[r.split(' ')[1]]}님이 나갔습니다.")
    return result