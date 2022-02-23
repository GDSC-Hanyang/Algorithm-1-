# 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    return x % sum(map(int, list(str(x)))) == 0