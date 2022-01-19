def solution(num):
    cnt = 0
    for _ in range(500):
        if num==1: break
        if num%2==0: num/=2
        else: num=3*num+1
        cnt+=1
    
    if num==1: return cnt
    return -1
