#음양 더하기
#https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    sum=0
    for k in range(len(signs)):
        if signs[k]==True:
            sum += absolutes[k]
        else:
            sum -= absolutes[k]
    answer = sum
    return answer
