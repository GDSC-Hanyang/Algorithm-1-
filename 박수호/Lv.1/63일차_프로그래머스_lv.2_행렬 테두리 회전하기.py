def solution(rows, columns, queries):
    answer = []
    data = [[x for x in range(1+columns*i, 1+columns*(i+1))] for i in range(rows)]
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        tmp = data[x1][y1]
        num = tmp
        for i in range(x1, x2):
            data[i][y1] = data[i+1][y1]
            num = min(num, data[i][y1])
        for i in range(y1, y2):
            data[x2][i] = data[x2][i+1]
            num = min(num, data[x2][i])
        for i in range(x2, x1, -1):
            data[i][y2] = data[i-1][y2]
            num = min(num, data[i][y2])
        for i in range(y2, y1+1, -1):
            data[x1][i] = data[x1][i-1]
            num = min(num, data[x1][i])
        data[x1][y1+1] = tmp
        answer.append(num)
    return answer