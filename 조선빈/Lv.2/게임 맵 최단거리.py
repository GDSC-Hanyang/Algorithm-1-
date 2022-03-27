from collections import deque

d = [[1,0], [-1, 0], [0,1], [0,-1]]

def solution(maps):
    r = len(maps)
    c = len(maps[0])
    t = [[-1 for _ in range(c)] for _ in range(r)]
    q = deque()
    q.append([0,0])
    t[0][0] = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            y_ = y + d[i][0]
            x_ = x + d[i][1]

            if -1<y_<r and -1<x_<c:
                if maps[y_][x_] == 1:
                    if t[y_][x_] == -1:
                        t[y_][x_] = t[y][x] + 1
                        q.append([y_, x_])

    answer = t[-1][-1]
    return answer
