def solution(expression):
    data = []
    tmp = ""
    for i in expression:
        if i.isnumeric():
            tmp += i
        else:
            data.append(tmp)
            data.append(i)
            tmp = ""
    data.append(tmp)
    ans = 0
    for i in [["*", "+", "-"], ["*", "-", "+"], ["+", "*", "-"], ["+", "-", "*"], ["-", "+", "*"], ["-", "*", "+"]]:
        data1 = data[:]
        while len(data1) != 1:
            while data1.count(i[0]) != 0:
                idx = data1.index(i[0])
                data1[idx-1] = str(eval(data1[idx-1] + i[0] + data1[idx+1]))
                del data1[idx]
                del data1[idx]
            while data1.count(i[1]) != 0:
                idx = data1.index(i[1])
                data1[idx-1] = str(eval(data1[idx-1] + i[1] + data1[idx+1]))
                del data1[idx]
                del data1[idx]
            while data1.count(i[2]) != 0:
                idx = data1.index(i[2])
                data1[idx-1] = str(eval(data1[idx-1] + i[2] + data1[idx+1]))
                del data1[idx]
                del data1[idx]
        ans = max(ans, abs(int(data1[0])))
    return ans