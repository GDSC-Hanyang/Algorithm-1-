def solution(s):
    answer = []
    s = s.split(' ')

    for i in range(len(s)):
        t = ''
        for j in range(len(s[i])):
            if j % 2 == 0:
                t += s[i][j].upper()
            else:
                t += s[i][j].lower()

        answer.append(t)

    return ' '.join(answer)
