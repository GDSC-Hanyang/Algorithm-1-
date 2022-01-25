def solution(n, lost, reserve):
    
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    answer = n - len(lost)
    
    for i in lost:
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)
        elif i+1 <= n and i+1 in reserve:
            answer += 1
            reserve.remove(i+1)

    return answer
