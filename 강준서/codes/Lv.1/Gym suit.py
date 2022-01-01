def solution(n, lost, reserve):
    answer = n - len(lost)

    lost=sorted(lost)
    reserve=sorted(reserve)

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                answer+=1
                lost[i]=-10
                reserve[j]=-20

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i]-1 == reserve[j]:
                answer+=1
                lost[i]=-10
                reserve[j]=-20
            if lost[i]+1 == reserve[j]:
                answer+=1
                lost[i]=-10
                reserve[j]=-20

    return answer
