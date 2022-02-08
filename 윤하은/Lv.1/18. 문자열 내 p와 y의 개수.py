def solution(s):
    answer = True

    pCount = [pos for pos, char in enumerate(s) if (char == 'p') or (char == 'P')]
    yCount = [pos for pos, char in enumerate(s) if (char == 'y') or (char == 'Y')]

    if len(pCount) == len(yCount) : 
        if len(pCount) != 0 : answer = True
    else : answer = False

    return answer