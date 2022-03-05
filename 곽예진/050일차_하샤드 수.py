#하샤드 수
#https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer=0
    for i in str(x):
        answer= answer+int(i)
    return True if x%answer==0 else False
