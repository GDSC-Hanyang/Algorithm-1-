# 부족한 금액 계산하기
# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = -1
    payment = 0
    for i in range(count):
        payment += price * (i + 1)
    answer = payment - money
    if answer > 0: return answer
    else: return 0