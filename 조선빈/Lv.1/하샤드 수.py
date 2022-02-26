def solution(x):
    a =  sum(map(int,list(str(x))))
    answer = (x%a==0)
    return answer
