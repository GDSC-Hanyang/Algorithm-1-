def solution(n, lost, reserve):
    #빌려줄 수 있는 친구들
    r=list(set(reserve)-set(lost))
    lost=list(set(lost)-set(reserve))
    print(reserve)
    print(lost)

    for x in r:
        if x-1 in lost:
            lost.remove(x-1)
        elif x+1 in lost:
            lost.remove(x+1)
    answer=n-len(lost)
    return answer