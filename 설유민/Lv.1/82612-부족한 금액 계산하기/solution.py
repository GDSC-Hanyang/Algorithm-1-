def solution(price, money, count):
    return max(price * (count * (count + 1) // 2) - money, 0)