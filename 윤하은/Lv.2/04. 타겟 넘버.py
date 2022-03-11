from collections import deque

def solution(numbers, target):

    global cnt
    cnt = 0

    def DFS(index, Nsum) :
        global cnt
        if index < len(numbers) :
            leaf = [-numbers[index], numbers[index]]
            DFS(index + 1, Nsum + leaf[0])
            DFS(index + 1, Nsum + leaf[1])
        
        elif index == len(numbers) :
            if Nsum == target :
                cnt += 1
            return cnt
    
    DFS(0,0)
            
    return cnt