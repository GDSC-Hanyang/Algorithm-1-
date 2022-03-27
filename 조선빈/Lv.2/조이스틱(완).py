def solution(name):
    A = []
    L = len(name)
    O = [L-1]  

    for i in name:
        add = min(ord(i)-ord('A'),26-ord(i)+ord('A'))
        A.append(add)

    for r in range(L,0,-1):
        while l and A[l]==0: 
            l-=1
        add = min(l+2*(L-r),l*2+L-r)
        O.append(add)
    
    for l in range(L): 
        r = l + 1
        while r<L-1 and A[r]==0: 
            r+=1 
        add = min(l*2+L-r,l+2*(L-r))
        O.append(add) 

    answer = sum(A)+min(O)
    return answer
