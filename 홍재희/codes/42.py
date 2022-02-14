# 자연수 뒤집어 배열로 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = list(str(n))
    answer.reverse()
    return list(map(int, answer))