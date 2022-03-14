def isThereP(x, y, tmp):
    # 위 왼 아래 오른
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < 5 and 0 <= ty < 5 and not tmp[tx][ty] == 'X':
            if tmp[tx][ty] == 'P':
                return True
            for i in range(4):
                sx = tx + dx[i]
                sy = ty + dy[i]
                if 0 <= sx < 5 and 0 <= sy < 5 and not (sx == x and sy == y) and tmp[sx][sy] == 'P':
                    return True
    return False

def solution(places):
    answer = []
    for place in places:
        tmp = []
        guridugi = 1
        for row in place:
            tmp.append([x for x in row])
        for i in range(5):
            for j in range(5):
                if tmp[i][j] == 'P':
                    print(f"P : {i},{j}")
                    if isThereP(i, j, tmp):
                        guridugi = 0
        answer.append(guridugi)
    return answer