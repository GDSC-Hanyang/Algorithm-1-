def solution(d, budget):
    answer = 0
    for i in sorted(d):
        budget-=i
        if(budget<0): break
        else: answer+=1

    return answer
  
