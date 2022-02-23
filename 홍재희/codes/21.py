# 최소 직사각형
# https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    return max([max(x) for x in sizes]) * max([min(x) for x in sizes])