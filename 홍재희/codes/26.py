# 다트게임
# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    # 점수|보너스|[옵션]
    # 옵션은 없을 수도 있다.
    answer = 0
    scores = []
    i = 0
    bonus = ['S', 'D', 'T']
    while i < len(dartResult):
        s = 0
        ctrl = 0
        if dartResult[i + 1] == '0':
            s = pow(10, bonus.index(dartResult[i + 2]) + 1)
            ctrl = 1
        else:
            s = pow(int(dartResult[i]), bonus.index(dartResult[i + 1]) + 1)
        #print(s, int(dartResult[i]), bonus.index(dartResult[i + 1]), dartResult[i + 1], i)
        if i + 2 + ctrl < len(dartResult) and dartResult[i + 2 + ctrl] == '#':
            scores.append(- s)
            i += (3 + ctrl)
        elif i + 2 + ctrl < len(dartResult) and dartResult[i + 2 + ctrl] == '*':
            if len(scores) == 0:
                scores.append(s * 2)
            else:
                scores[len(scores) - 1] *= 2
                scores.append(s * 2)
            i += (3 + ctrl)
            #print(i, '*')
            #print(i < len(dartResult))
        else:
            scores.append(s)
            i += (2 + ctrl)
    answer = sum(scores)
    return answer
#print(solution('1S2D*3T'))
print(solution('1D2S#10S'))