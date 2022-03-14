from collections import deque

def bfs(p):
    Ps = []

    for i in range(5): # P의 좌표
        for j in range(5):
            if p[i][j] == 'P':
                Ps.append([i, j])

    for s in Ps:
        que = deque([s])  # 큐에 초기 P의 좌표
        visit = [[0]*5 for i in range(5)]   # 방문 리스트
        distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
        visit[s[0]][s[1]] = 1

        while que:
            y, x = que.popleft()

            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visit[ny][nx] == 0:

                    if p[ny][nx] == 'O':
                        que.append([ny, nx])
                        visit[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1

                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []

    for i in places:
        answer.append(bfs(i))

    return answer
