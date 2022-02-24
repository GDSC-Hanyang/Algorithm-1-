# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    i = 1
    while i < len(s):
        x = [s[j*i:j*i+i] for j in range(int(len(s)/i))]
        y = ''
        z = []
        c = 1
        j = int(len(s)/i)
        if ''.join(x) != s: x.append(s[j*i:])
        i += 1
        for k in x:
            if y != k:
                z.append(k)
                c = 1
            else:
                z.pop()
                c += 1
                z.append(str(c) + k)
            y = k
        if len(''.join(z)) < answer: answer = len(''.join(z))
    return answer