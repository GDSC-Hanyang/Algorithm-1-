# 시저 암호
# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif 97 <= ord(i) <= 122:
            answer += chr(97 + (ord(i) + n - 97) % 26)
        else: # 65 <= ord(i) <= 90
            answer += chr(65 + (ord(i) + n - 65) % 26)
    return answer