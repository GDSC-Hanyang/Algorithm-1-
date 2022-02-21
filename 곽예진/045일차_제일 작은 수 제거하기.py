#제일 작은 수 제거하기
#https://programmers.co.kr/learn/courses/30/lessons/12935

#for 반복문에서 가장 작은 수 찾아서 리스트에서 제거하기-복잡해
#sort함수에서 가장 작은 숫자를 찾아서 배열에서 제거하기-nice

def solution(arr):
    b=sorted(arr)[0]
    arr.remove(b)
    if arr==[]:
        arr=[-1]
    return arr
  
#숫자 제거 remove,del,pop 함수등 존재


#[가장 작은 수]제거
##[1]번 방법. b = min(arr)
##[2]번 방법. sorted로 정렬하고 index[0]
