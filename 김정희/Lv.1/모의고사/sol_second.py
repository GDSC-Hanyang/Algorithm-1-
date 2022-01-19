def solution(answers):
    a1=[1,2,3,4,5]
    a2=[2,1,2,3,2,4,2,5]
    a3=[3,3,1,1,2,2,4,4,5,5]
    c=[0,0,0]
    # 적은거는 이렇게 배열을 한번에 만들어두는게 좋다 ~~
    for i, x in enumerate(answers):
        i+=1
        i1=i%5 -1 if i%5!=0 else 4
        i2=i%8 -1 if i%8!=0 else 7
        i3=i%10 -1 if i%10!=0 else 9
        if x==a1[i1]:
            c[0]+=1
        if x==a2[i2]:
            c[1]+=1
        if x==a3[i3]:
            c[2]+=1
    m=max(c)
    answer=[]
    for i,x in enumerate(c):
        if x==m:
            answer.append(i+1)
    return answer