def comparison(answers, math1, math2, math3):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for t in range(0,len(answers)):
        if answers[t] == math1[t]:
            cnt1 += 1
        if answers[t] == math2[t]:
            cnt2 += 1
        if answers[t] == math3[t]:
            cnt3 += 1
    if cnt1>cnt2:
        if cnt1>cnt3:
            return [1]
        if cnt1<cnt3:
            return [3]
        if cnt1==cnt3:
            return [1,3]
    if cnt1<cnt2:
        if cnt2>cnt3:
            return [2]
        if cnt2<cnt3:
            return [3]
        if cnt2==cnt3:
            return [2,3]
    if cnt1==cnt2:
        if cnt1>cnt3:
            return [1,2]
        if cnt1<cnt3:
            return [3]
        if cnt1==cnt3:
            return [1,2,3]
        

def solution(answers):
    answer = []
    math1 = []
    math2 = []
    math3 = []
    for i in range(0,201):
        for j in range(1,6):
            math1.append(j)
        for k in [2,1,2,3,2,4,2,5]:
            math2.append(k)
        for l in [3,3,1,1,2,2,4,4,5,5]:
            math3.append(l)
            
    answer = comparison(answers, math1, math2, math3)
    
    return answer
