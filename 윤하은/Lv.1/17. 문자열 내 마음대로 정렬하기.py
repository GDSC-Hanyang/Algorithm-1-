def solution(strings, n):
    orderAlpha = []
    sameAlpha = []
    temp = []
    answer = []

    #리스트 orderAlpha에 strings의 i번째 원소와 n 번째 인덱스 값 저장
    for i in range(len(strings)) :
        orderAlpha.append([strings[i], strings[i][n]])

    #n 번째 인덱스 값 오름차순 정렬
    orderAlpha.sort(key=lambda x:x[1])

    #n 번째 인덱스 값이 동일한 것끼리 sameAlpha에 저장 후 사전 순 정렬
    i = 0
    while i < len(orderAlpha) :
        for x in range(len(orderAlpha)) :
            if orderAlpha[i][1] == orderAlpha[x][1] :
                sameAlpha.append(orderAlpha[x])
        sameAlpha.sort(key=lambda x:x[0])

    #저장한 sameAlpha의 원소들을 임시 리스트 temp에 할당
        temp.extend(sameAlpha)

    #sameAlpha를 빈 배열로 만들고 i값 업데이트    
        i = i + len(sameAlpha)
        sameAlpha = []

    #튜플로 저장한 temp 원소의 첫 번째 값만 리스트 answer에 할당
    for i in range(len(temp)):
        answer.append(temp[i][0]) 

    return answer