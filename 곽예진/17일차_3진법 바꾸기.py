#3진법 바꾸기
#https://programmers.co.kr/learn/courses/30/lessons/68935
#난이도 중

def solution(n):
    #10진법 -> 3진법
    count=0
    num_3=0
    while n > 0 :
        num_3 += (n%3)*(10**count)
        n = n//3
        count += 1
    print(num_3)
    
    #앞뒤 반전
    rev=0
    count=0
    for i in str(num_3):
        rev += int(i)*(10**count)
        count += 1
    print(rev)
    
    #3진법 -> 10진법
    num_10=0
    count=0
    for r in str(rev):
        num_10 += int(r)*(3**(len(str(rev))-count-1))
        count += 1
        
    return num_10
    

