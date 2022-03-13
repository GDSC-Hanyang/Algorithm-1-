def solution(rows, columns, queries):
    answer = []
    array = [[0 for colum in range(columns)] for row in range(rows)]
    t = 1
    for row in range(rows):
        for colum in range(columns):
            array[row][colum] = t
            t += 1

    for x1,y1,x2,y2 in queries:
        tmp = array[x1-1][y1-1]
        Min = tmp

        for k in range(x1-1,x2-1): 
            test = array[k+1][y1-1]
            array[k][y1-1] = test
            Min = min(Min, test)

        for k in range(y1-1,y2-1): 
            test = array[x2-1][k+1]
            array[x2-1][k] = test
            Min = min(Min, test)

        for k in range(x2-1,x1-1,-1): 
            test = array[k-1][y2-1]
            array[k][y2-1] = test
            Min = min(Min, test)

        for k in range(y2-1,y1-1,-1): 
            test = array[x1-1][k-1]
            array[x1-1][k] = test
            Min = min(Min, test)

        array[x1-1][y1] = tmp
        answer.append(Min)

    return answer
  
  def solution(rows, columns, queries):
    answer = []

    board = [[i+(j)*columns for i in range(1,columns+1)] for j in range(rows)]
    # print(board)

    for a,b,c,d in queries:
        stack = []
        r1, c1, r2, c2 = a-1, b-1, c-1, d-1


        for i in range(c1, c2+1):

            stack.append(board[r1][i])
            if len(stack) == 1:
                continue
            else:
                board[r1][i] = stack[-2]


        for j in range(r1+1, r2+1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]

        for k in range(c2-1, c1-1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]

        for l in range(r2-1, r1-1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        answer.append(min(stack))


    return answer
