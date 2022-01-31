#모의고사
#https://programmers.co.kr/learn/courses/30/lessons/42840
#난이도 중하

def solution(answers):
    person1=[1,2,3,4,5]
    person2=[2,1,2,3,2,4,2,5]
    person3=[3,3,1,1,2,2,4,4,5,5]
    
    count1,count2,count3 = 0,0,0
    for i in range(len(answers)):
        if answers[i]==person1[i%5]:
            count1 +=1
        if answers[i]==person2[i%8]:
            count2 +=1
        if answers[i]==person3[i%10]:
            count3 +=1
    
    if count1==count2:
        if count1==count3:
            answer=[1,2,3]
        elif count1>count3:
            answer=[1,2]
        else:
            answer=[3]
    elif count1>count2:
        if count1==count3:
            answer=[1,3]
        elif count1>count3:
            answer=[1]
        else:
            answer=[3]
    else:
        if count2==count3:
            answer=[2,3]
        elif count2>count3:
            answer=[2]
        else:
            answer=[3]
    return answer
