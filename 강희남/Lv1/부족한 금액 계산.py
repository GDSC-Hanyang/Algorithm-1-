def solution(price, money, count):
    total_price =  (price)*(count)*(count+1)/2
    return total_price - money if money < total_price else 0

"""
참 if 조건 else 거짓 - 조건(대소비교) -> max(), min()
    def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
"""