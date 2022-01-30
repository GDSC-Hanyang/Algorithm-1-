def solution(n, lost, reserve):
    R = set(reserve)-set(lost)
    L = set(lost)-set(reserve)
    for i in R:
        if i-1 in L:
            L.remove(i-1)
        elif i+1 in L:
            L.remove(i+1)
    answer = n-len(L)
    return answer
