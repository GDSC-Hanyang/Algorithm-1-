def solution(n):
    tmp = []
    while True:
        if n // 3 == 0:
            tmp.append(str(n % 3))
            break
        tmp.append(str(n % 3))
        n = n // 3
    answer = 0
    for i in range(len(tmp)):
        answer += (3**(len(tmp)-i-1))*int(tmp[i])
    return answer