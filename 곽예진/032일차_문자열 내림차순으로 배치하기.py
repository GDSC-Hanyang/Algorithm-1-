#문자열 내림차순으로 배치하기
#https://programmers.co.kr/learn/courses/30/lessons/12917
  
def solution(s):
    lista=[]
    for i in s:
        lista.append(i)
    lista.sort(reverse=True)
    print(lista)
    answer=''
    for i in lista:
        answer+= str(i)
    return answer  
