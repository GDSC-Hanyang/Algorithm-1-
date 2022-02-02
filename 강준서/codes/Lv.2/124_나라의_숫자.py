def solution(n):
    answer = ''
    while n: 
        if n%3==0:
            answer+='4'
            n = n//3-1
        else:
            if n%3==1: answer+='1'
            else: answer+='2'
            n = n//3
    return answer[::-1]
