def solution(array, commands):
    answer=[]
    for c in commands:
        a=array[c[0]-1:c[1]]
        a.sort()
        answer.append(a[c[2]-1])
    return answer