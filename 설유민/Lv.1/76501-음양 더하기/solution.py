def solution(absolutes, signs):
    for index in range(0, len(signs)):
        if signs[index] == False:
            absolutes[index] *= -1
    answer = sum(absolutes)
        
    return answer
