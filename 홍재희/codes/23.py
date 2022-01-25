def solution(price, money, count):
    answer = -1
    payment = 0
    for i in range(count):
        payment += price * (i + 1)
    answer = payment - money
    if answer > 0: return answer
    else: return 0