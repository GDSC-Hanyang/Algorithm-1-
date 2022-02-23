#정수 내림차순으로 배치하기
#https://programmers.co.kr/learn/courses/30/lessons/12933

#[1]방법. 한개씩 분리해서 sort 써서 정렬 후 다시 붙이기
def solution(n):
    #answer리스트에 숫자 한개씩 떼어내기
    answer=[]
    for i in str(int(n)):
        answer.append(i)
    #숫자 정렬
    answer.sort(reverse=True)
    #리스트 숫자 더해서 정수 변환
    r_an=''
    for i in answer:
        r_an+=i
    return int(r_an)
    
#[2]방법. 크기비교하면서 한개씩 붙이기-첫번째 시작점이 애매함=>별로

# [join함수]
#리스트에서 요소 더해서 결과 나오는 함수 = "join함수"

''.join()

#best
#[3]방법. ''.join()이용

def solution(n):
    answer=[]
    for i in str(int(n)):
        answer.append(i)
    answer.sort(reverse=True)
    #리스트 숫자 더해서 정수 변환
    return int(''.join(answer))
