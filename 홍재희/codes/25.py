# 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = ''
    ls = len(s)
    answer = s[int(ls / 2 - 0.5):int(ls / 2 + 1.5)] if ls % 2 == 0  else s[int(ls/2)]
    return answer