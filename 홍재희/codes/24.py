# 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    for i in range(n):
        num1 = bin(arr1[i])[2:]
        num2 = bin(arr2[i])[2:]
        map1.append('0' * (n - len(num1)) + num1)
        map2.append('0' * (n - len(num2)) + num2)
    for i in range(n):
        map3 = ''
        for j in range(n):
            if map1[i][j] == '0' and map2[i][j] == '0':
                map3 += ' '
            else:
                map3 += '#'
        answer.append(map3)
    return answer