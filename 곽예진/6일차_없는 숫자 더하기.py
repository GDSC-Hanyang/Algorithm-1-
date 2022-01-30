#없는 숫자 더하기
#https://programmers.co.kr/learn/courses/30/lessons/86051
#난이도 하

def solution(numbers):
    addsum=0
    #인덱스 활용하기
    for i in range(10):
        addsum += i
    for k in numbers:
        addsum -= k
    answer = addsum
    return answer
