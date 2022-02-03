#최소직사각형
#https://programmers.co.kr/learn/courses/30/lessons/86491
#난이도 중하

def solution(sizes):
    maxlist=[]
    maxw=0
    maxh=0
    for i in sizes:
        i.sort()
        print(i)
        a=i[0]
        b=i[1]
        if a>maxw:
            maxw=a
        if b>maxh:
            maxh=b
        
        print(maxw,maxh)
    answer = maxw*maxh
    
    return answer

-----------------------------------------------
#이렇게도 표현 가능
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
