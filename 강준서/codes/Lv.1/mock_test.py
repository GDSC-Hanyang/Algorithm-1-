def solution(answers):
    one = list(range(1,6))*2000
    two = [2, 1, 2, 3, 2, 4, 2, 5]*1250
    three = [3,3,1,1,2,2,4,4,5,5,]*1000

    scores=[0,0,0]

    for i, ans in enumerate(answers):
        if ans == one[i]: scores[0]+=1
        if ans == two[i]: scores[1]+=1
        if ans == three[i]: scores[2]+=1

    _dict = dict(zip([1,2,3],scores))

    answer = []

    mx = max(_dict.values())

    for i in _dict:
        if mx == _dict[i] : answer.append(i)

    return sorted(answer)
