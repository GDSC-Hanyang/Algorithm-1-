def solution(s):
    answer = list(map(int, s.split()))
    return str(min(answer))+' '+str(max(answer))
