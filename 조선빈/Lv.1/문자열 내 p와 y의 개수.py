def solution(s):
    answer = True
    s = s.lower()
    cntP = 0
    cntY = 0
    for i in s:
        if i == 'p':
            cntP += 1
        if i == 'y':
            cntY += 1

    if cntP == cntY:
        answer = True
    else:
        answer = False

    return answer
