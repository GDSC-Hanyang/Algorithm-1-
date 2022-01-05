# 키패드 누르기
# 2022-01-04
# https://programmers.co.kr/learn/courses/30/lessons/67256

X = [2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 3]
Y = [4, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4]

def distance(a, b):
    return abs(X[a] - X[b]) + abs(Y[a] - Y[b])

def solution(numbers, hand):
    answer = ''
    left = 10 # 10 = *
    right = 11 # 11 = #
    for i in numbers:
        if X[i] == 2:
            #distance = i의 좌표 - 손가락의 좌표
            if distance(i, left) == distance(i, right):
                if hand =='left':
                    answer += 'L'
                    left = i
                else:
                    answer += 'R'
                    right = i
            elif distance(i, left) > distance(i, right):
                answer += 'R'
                right = i
            else:
                answer += 'L'
                left = i
        elif X[i] == 1:
            answer += 'L'
            left = i
        else:
            answer += 'R'
            right = i
    return answer