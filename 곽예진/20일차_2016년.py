#2016년
#https://programmers.co.kr/learn/courses/30/lessons/12901
#난이도 중

def solution(a, b):
    #날짜 구하기
    if a==1:
        c=b
    if a==2:
        c=b+31
    if a%2==1 and a>=3: #홀수
        if a<9:
            c=b+(31+29)+(31+30)*((a-3)/2)
        else:
            c=b+(31+29)+(31+30)*((a-3)/2)+1
    if a%2==0 and a>=4: #짝수
        c=b+(31*2+29)+((a-4)/2)*(31+30)
    #요일 구하기
    day=['THU','FRI','SAT','SUN','MON','TUE','WED']
    i = int(c%7)
    answer = day[i]
    return answer
