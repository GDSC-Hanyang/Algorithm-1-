def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        move -= 1
        for c in range(len(board)):
            if board[c][move] != 0:
                bucket.append(board[c][move])
                board[c][move] = 0
                if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
                    bucket = bucket[:-2]
                    answer += 2
                break
    return answer