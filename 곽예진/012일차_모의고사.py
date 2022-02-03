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

##다른분 풀이
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []
#enumerate는 index와 item 둘다를 나타내준다.
    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
