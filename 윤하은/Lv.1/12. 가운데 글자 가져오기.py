def solution(s):
    sList = list(s)
    answer = ''.join(sList[(len(sList)-1)//2 : len(sList)//2+1])
    return answer