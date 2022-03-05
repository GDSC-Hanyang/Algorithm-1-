#행렬의 덧셈
#https://programmers.co.kr/learn/courses/30/lessons/12950

#일반 풀이
def solution(arr1, arr2):
    answer=[]
    for i in range(len(arr1)):
        element=[]
        for k in range(len(arr1[0])):
            element.append(arr1[i][k]+arr2[i][k])
        answer.append(element)
    return answer
#zip 활용1  
def solution(arr1, arr2):
    answer=[]
    for i in range(len(arr1)):
        element=[]
        for k in zip(arr1[i],arr2[i]):
            element.append(sum(k))
        answer.append(element)
    return answer

#best 
#zip 활용2   
def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1,arr2)]
    return answer
