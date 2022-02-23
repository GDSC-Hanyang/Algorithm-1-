#콜라츠 추측
#https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    count=0
    while num != 1 and count < 500 :
        count += 1
        if num%2 ==0: #짝수일때
            num= num / 2
        else: #홀수일때
            num= num*3 + 1
    if count>=500:
        count=-1
    return count
