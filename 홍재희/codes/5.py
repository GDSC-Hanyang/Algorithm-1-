# 크레인 인형뽑기 게임
# 2022-01-05
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    num =  len(board)
    basket = []
    for i in moves:
        for j in range(num):
            if not(board[j][i-1] == 0):
                if len(basket) > 0 and basket[-1] == board[j][i-1]:
                    answer += 1
                    del basket[-1]
                    board[j][i-1] = 0
                else:
                    basket.append(board[j][i-1])
                    board[j][i-1] = 0
                break
    return answer * 2