def solution(a, b):
    answer = 0
    nMax = b
    nMin = a

    if nMax < nMin :
        nMax = a
        nMin = b

    for i in range(nMin, nMax+1) : answer += i

    return answer