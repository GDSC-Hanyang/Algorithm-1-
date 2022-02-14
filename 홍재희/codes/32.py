# 문자열 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    arr = [ord(i) for i in s]
    arr.sort(reverse=True)
    arr = [chr(i) for i in arr]
    answer = ''.join(arr)
    return answer