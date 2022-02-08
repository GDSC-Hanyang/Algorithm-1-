#같은 숫자는 싫어
#https://programmers.co.kr/learn/courses/30/lessons/12906
#난이도 중

def solution(arr):
    answer=[]
    answer.append(arr[0])
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i+1])
    return answer
