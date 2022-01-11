def solution(a, b):
    answer=sum(a*b for a,b in zip(a,b))
    return answer