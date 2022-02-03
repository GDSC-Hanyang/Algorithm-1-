#약수의 개수와 덧셈
#https://programmers.co.kr/learn/courses/30/lessons/77884
#난이도 하

def solution(left, right):
    result=0
    for i in range(left,right+1):
        count=0
        for k in range(1,i+1):
            if (i % k == 0): #약수 찾기
                count +=1
        if count%2==0: #약수의 개수가 짝수인 경우
            result += i   
        else:
            result -= i
    
    return result
