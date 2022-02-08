#가운데 글자 가져오기
#https://programmers.co.kr/learn/courses/30/lessons/12903
#난이도 하

def solution(s):
    if len(s)%2==0:
        answer=s[int(len(s)/2-1):int(len(s)/2+1)]
    else:
        answer=s[int(len(s)/2)]
    
    return answer
