def solution(answers):
    a1=0
    a2=0
    a3=0
    for i, x in enumerate(answers): #enumerate = 인덱스, 값의 튜플의 iterator
        i=i+1
        # 1번 친구
        if (x != 0 and i%5==x) or (i%5==0 and x==5):
            a1+=1
        # 2번 친구
        if i%2==1 and x==2:
            a2+=1
        elif i%2==0:
            ii=i%8
            if ii==2 and x==1:
                a2+=1
            elif ii==4 and x==3:
                a2+=1
            elif ii==6 and x==4:
                a2+=1
            elif ii==0 and x==5:
                a2+=1
        # 3번 친구
        k=i%10
        if (k==1 or k==2) and x==3:
            a3+=1
        elif (k==3 or k==4) and x==1:
            a3+=1
        elif (k==5 or k==6) and x==2:
            a3+=1
        elif (k==7 or k==8) and x==4:
            a3+=1
        elif (k==9 or k==0) and x==5:
            a3+=1
    q=[a1,a2,a3]
    print(q)
    m=max(q)
    answer=[]
    for id,vl in enumerate(q):
        if m==vl:
            answer.append(id+1)
    return answer

#멍청노가다입니다