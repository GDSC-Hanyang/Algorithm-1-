#평균 구하기
#https://programmers.co.kr/learn/courses/30/lessons/12944

#[1]번 생각.하나씩 더해서 len(arr)로 나누기 => bad
#[2]번 생각.숫자열을 한번에 더하기 => good

def solution(arr):
    return sum(arr)/len(arr)
