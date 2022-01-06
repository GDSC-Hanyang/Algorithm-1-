def solution(lottos, win_nums):
    answer = []
    zeros=0
    for i in lottos:
        if(i==0) : zeros+=1
    correct = list(set(lottos).intersection(set(win_nums)))

    _dict = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    answer.append(_dict[len(correct)+zeros])
    answer.append(_dict[len(correct)])
    return answer
    
