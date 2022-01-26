def solution(dartResult):
    cnt = 0
    data = ["", "", "", ""]
    num = "0"
    for i in dartResult:
        if i.isdecimal():
            if i == '0' and num == '1':
                num = '10'
            else:
                data[cnt] += num
                cnt += 1
                num = i
        else:
            if i == 'D': num += "**2"
            elif i == 'T': num += "**3"
            elif i == '*':
                data[cnt-1] += "*2"
                num += "*2"
            elif i == '#': num += "*(-1)"
            else: num += "**1"
    data[3] += num
    return eval("+".join(data))