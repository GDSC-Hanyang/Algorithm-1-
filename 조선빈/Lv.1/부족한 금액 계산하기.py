def solution(price, money, count):
    answer = -1
    Sum = 0
    for cnt in range(1,count+1):
        Sum += price * cnt
    if Sum > money:
        answer = Sum - money
    else:
        answer = 0
    return answer
