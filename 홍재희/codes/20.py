# 2016년
# 2022-01-20
# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    weekDay = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    print(day[:(a-1)])
    num = sum(day[:(a-1)]) + b
    answer = weekDay[num % 7 - 1]
    return answer