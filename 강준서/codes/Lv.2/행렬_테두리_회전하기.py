# 빡구현 문제 입니다,,,, ㅠㅠ
# while문 4번 쓴 것이 좀 지저분해 보이기는 하지만, 어차피 성능은 괜찮은 편이니..
# 한가지 while문으로 줄이는 방법으로는 i,j 위치를 중간에 바꾸기? 방향 인자로 1, -1을 곱해주기?
# 그런데 굳이 그렇게까지 투자하고 싶지는 않았습니다...

def solution(rows, columns, queries):
    M = [[i*columns+j for j in range(1,columns+1)] for i in range(rows)]
    answer = []

    for query in queries:
        si, sj, ei, ej = tuple(query)
        i,j = si-1,sj-1   # 시작점은 좌측 상단
        temp = M[i][j]
        min_ = temp

        # 먼저 오른쪽으로 이동
        while True: 
            if j == ej-1: break
            M[i][j+1], temp = temp, M[i][j+1]
            min_ = min(min_,temp)
            j+=1
        
        # 아래로 이동
        while True:
            if i == ei-1: break
            M[i+1][j], temp = temp, M[i+1][j]
            min_ = min(min_,temp)
            i+=1
        
        # 왼쪽으로 이동 
        while True:
            if j == sj-1: break
            M[i][j-1], temp = temp, M[i][j-1]
            min_ = min(min_,temp)
            j-=1
        
        # 위로 이동
        while True:
            if i == si-1: break
            M[i-1][j], temp = temp, M[i-1][j]
            min_ = min(min_,temp)
            i-=1

        answer.append(min_)

    return answer
