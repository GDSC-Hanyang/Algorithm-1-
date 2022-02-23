# 제일 작은 수 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    num = min(arr)
    arr.remove(num)
    if len(arr) == 0:
        return [-1]
    else:
        return arr