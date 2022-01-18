def solution(lottos, win_nums): 
    num = len(set(lottos) & set(win_nums))
    zero_num = lottos.count(0)
    answer = [7-num-zero_num if num != 0 else 1 if num == 0 and zero_num != 0 else 6, 7-num if num != 0 else 6]
    return answer