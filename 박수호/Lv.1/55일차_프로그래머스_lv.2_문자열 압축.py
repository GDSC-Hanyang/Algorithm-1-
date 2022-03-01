def solution(s):
    num = len(s)
    for steps in range(1, len(s)+1):
        answer = ""
        data = [s[i:i + steps] for i in range(0, len(s), steps)]
        before = data[0]
        cnt = 1
        for i in range(1, len(data)):
            if before == data[i]:
                cnt += 1
            else:
                tmp = str(cnt) if cnt > 1 else ""
                answer += tmp + before
                before = data[i]
                cnt = 1
        tmp = str(cnt) if cnt > 1 else ""
        answer += tmp + before
        num = min(num, len(answer))
    return num