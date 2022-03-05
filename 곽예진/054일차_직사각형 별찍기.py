#직사각형 별찍기
#https://programmers.co.kr/learn/courses/30/lessons/12969

#a,b 중요
a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*'*a)
    
    
#strip()
문자열의 맨앞과 맨뒤의 공백을 제거해주는 함수

#split()
('')안에 들어가는 문자를 중심으로 구분한다.
a='1. 2. 3. 4. '
예를 들어 split(' ')처럼 공백이 들어있으면 공백을 중심으로 나뉜다.=> ['1.','2.','3.','4.']
split('. ')은 . 을 기준으로 문자열이 구분된다.=>['1','2','3','4']
