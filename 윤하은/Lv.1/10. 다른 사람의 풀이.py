def solution(price, money, count):
    compare = price * count * (count + 1) / 2
    if money >= compare : answer = 0
    else : answer = compare - money
    return answer