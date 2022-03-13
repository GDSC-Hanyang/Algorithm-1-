from collections import deque

# globals
X = [-1,0,1,0]
Y = [0,1,0,-1]
queue = deque([(0,0)])

def solution(maps):
    row = len(maps)
    col = len(maps[0])

    def IsRange(a,b):
        if a>=0 and b>=0 and a<row and b<col: return True
        return False

    visited = [[0 for _ in range(col)] for _ in range(row)]
    visited[0][0]=1
    while(queue):
        a,b = queue.popleft()
        for x,y in zip(X,Y):
            if(IsRange(a+x,b+y) and visited[a+x][b+y]==0):
                if maps[a+x][b+y] == 1:
                    queue.append((a+x,b+y))
                    visited[a+x][b+y]=visited[a][b]+1

    return visited[row-1][col-1] if visited[row-1][col-1] else -1
