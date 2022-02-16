def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        answer = True
    for i in s:
        if i.isalpha() == True:
            answer = False
    return answer
