def solution(board, moves):
    answer = 0
    basket = []
    for col_index in moves:
        row_index = 0
        for row_index in range(0, len(board)):
            if board[row_index][col_index - 1] != 0:
                basket.append(board[row_index][col_index - 1])
                board[row_index][col_index - 1] = 0
                if (len(basket) > 1) and (basket[-1] == basket[-2]):
                    answer += 2
                    basket.pop()
                    basket.pop()
                break
    
    return answer
