def solution(n):
    board = [True] * (n + 1)

    for i in range(2, int(n ** 0.5) + 1):
        if board[i] == True:  # 해당 숫자가 소수라면
            for j in range(2 * i, n + 1, i):
                board[j] = False
    return board.count(True) - 2