def solution(lottos, win_nums):
    answer = []
    min_num = 0
    add = 0
    max_num = 0
    i=0
    while i<=5:
        if lottos[i] in win_nums:
            min_num += 1
        if lottos[i] == 0:
            add += 1
        i += 1
    max_num = min_num + add
        
    if max_num == 2:
        win_max = 5
    elif max_num == 3:
        win_max = 4
    elif max_num == 4:
        win_max = 3
    elif max_num == 5:
        win_max = 2
    elif max_num == 6:
        win_max = 1
    else:
        win_max = 6
    answer.append(win_max)
    
    if min_num == 2:
        win_min = 5
    elif min_num == 3:
        win_min = 4
    elif min_num == 4:
        win_min = 3
    elif min_num == 5:
        win_min = 2
    elif min_num == 6:
        win_min = 1
    else:
        win_min = 6    
    answer.append(win_min)

    return answer
