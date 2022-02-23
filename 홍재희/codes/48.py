# 콜라츠 추측
# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    answer = 0
    while num != 1 and answer <= 500:
        answer += 1
        if num % 2 == 0: num /= 2
        else: num = num * 3 + 1
    if answer == 501: return -1
    else: return answer