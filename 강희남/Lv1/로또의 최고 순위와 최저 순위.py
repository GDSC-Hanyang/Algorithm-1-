def solution(lottos, win_nums):
    
    zero_count = 0
    count = 0
    
    for i in lottos :
        if i == 0 : zero_count+=1
        else :
            for j in win_nums :
                  if i == j : count+=1
                        
    highest_result = zero_count+count  
    lowest_result = count
    
    if highest_result == 0 : highest_result = 1
    if lowest_result == 0 : lowest_result = 1
    
    answer = [7-highest_result, 7-lowest_result]
    return answer