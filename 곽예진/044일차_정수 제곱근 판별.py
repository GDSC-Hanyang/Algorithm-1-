#정수 제곱근 판별
#https://programmers.co.kr/learn/courses/30/lessons/12934

#[1]번 생각.정수형이랑 루트 씌운거랑 같냐?
def solution(n):
    if n**(1/2) == float(int(n**(1/2))):
        answer=(n**(1/2)+1)**2
    else:
        answer=-1
    return answer
#n**1/2는 실수형이다. 그래서 float 안 씌우면 float == int로 되어 항상 틀림.



#[2]번 아이디어. 루트 씌운 숫자가 1로 나눈 나머지가 0이냐?
def solution(n):
    k= n**(1/2)
    if k%1 ==0:
        answer=(k+1)**2
    else:
        answer=-1
    return answer
