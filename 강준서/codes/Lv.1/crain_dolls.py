def solution(board, moves):
    answer = 0
    stack = []
    L = len(board)

    top = -1
    for i in moves:
        itr=0

        while(board[itr][i-1]==0):
            itr+=1
            if(itr==L-1):
                break

        if(top>=0 and stack[top]==board[itr][i-1]):
            del stack[top]
            answer+=2
            top-=1

        elif(board[itr][i-1]!=0):
            stack.append(board[itr][i-1])
            top+=1

        board[itr][i-1]=0

    return answer
