#예산
#https://programmers.co.kr/learn/courses/30/lessons/12982
#난이도 중

from itertools import combinations
def solution(d, budget):
    d.sort()
    answer=0
    if sum(d) <= budget: 
        return len(d)
    for i in range(len(d)):
        if sum(d[:i+1])<budget:
            answer += 1
        elif sum(d[:i+1])==budget:
            return answer+1
        else:
