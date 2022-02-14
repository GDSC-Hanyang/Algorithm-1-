# 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    arr = s.split(' ')
    arr2 = []
    result = ''
    for i in arr:
        for j in range(len(i)):
            if j % 2 == 0:
                result += i[j].upper()
            else:
                result += i[j].lower()
        result += ' '
    return result[:-1]