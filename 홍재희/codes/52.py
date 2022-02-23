# 행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        add = []
        for j in range(len(arr1[0])):
            add.append(arr1[i][j] + arr2[i][j])
        answer.append(add)
    return answer