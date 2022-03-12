def solution(name):
    moves = []
    L = len(name)
    LR = [L-1]  # 순서대로 가는 경우

    for i in name: moves.append(min(ord(i)-ord('A'),26-ord(i)+ord('A')))

    for left in range(L): # 일단 left까지는 순서대로 오른쪽으로 이동
        right = left + 1
        while right<L-1 and moves[right]==0: right+=1 # 'A'인 글자가 연속으로 있는 경우 
        LR.append(min(left*2+L-right,left+2*(L-right))) # 양옆으로 움직인 케이스 중 더 적게 움직인 것을 택함

    for right in range(L,0,-1): # right까지는 순서대로 왼쪽으로 이동
        left = right - 1
        while left and moves[left]==0: left-=1
        LR.append(min(left*2+L-right,left+2*(L-right)))

    return sum(moves)+min(LR)
  
