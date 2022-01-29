def solution(n):
    answer = 0
    List = []
    for x in range(1,n+1):
        if n%x == 1:
            List.append(x)
    answer = List[0]
    return answer
