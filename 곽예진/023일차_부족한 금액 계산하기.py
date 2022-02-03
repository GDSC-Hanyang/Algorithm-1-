#부족한 금액 계산하기
#https://programmers.co.kr/learn/courses/30/lessons/82612
#난이도 중하

def solution(price, money, count):
    sum=0
    for i in range(1,count+1):
        sum +=i
    result=sum*price-money
    if result<0:
        result=0

    return result
