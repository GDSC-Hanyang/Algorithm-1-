def solution(new_id):
    #Step1
    answer = new_id.lower()

    #Step2
    allowed = "-_."
    for i in answer :
        if(i.islower() or i.isdigit() or i in allowed) :
            continue
        else : 
            answer = answer.replace(i,'')

    #Step3
    targets = []
    for i, char in enumerate(answer) :
        if (i==0) : continue
        if(char == '.' and answer[i-1] =='.'):
            targets.append(i)

    for i, idx in enumerate(targets) :
        answer = answer[:idx]+answer[idx+1:]
        if(i+1 <= len(targets)-1) :
            targets[i+1] -= i+1

    #Step4
    if answer[0] == '.' :
        answer=answer[1:]

    leng = len(answer)-1
    if (leng>=0) :
        if answer[leng] == '.':
            answer=answer[:leng]

    #Step5
    if answer == '' :
        answer = 'a'

    #Step6
    if len(answer) >=16 :
        answer=answer[:15]
        if(answer[14]=='.') :
            answer = answer[:14]

    #Step7
    if len(answer) <=2 :
        rep = answer[len(answer)-1]
        while(len(answer)<3):
            answer+=rep

    return answer
