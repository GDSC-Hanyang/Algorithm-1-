# 크레인 인형뽑기 게임
#https://programmers.co.kr/learn/courses/30/lessons/64061
#난이도 중상...

def solution(board, moves):
 
    #[1]moves에 해당하는 인형종류숫자 board에서 뽑아내기
    toy_type=[]
    for i in moves:
        k=0
        while (board[k][i-1] == 0) and k!=len(board)-1:
            k=k+1
        toy_type.append(board[k][i-1])
        board[k][i-1]=0
    #[2] 0지우기        
    while 0 in toy_type:
        toy_type_2=[]
        for r in toy_type:
            if r != 0:
                toy_type_2.append(r)   
        toy_type=toy_type_2
    #[3] 겹치는 숫자항 지우기    
    count=0
    q=0
    while q < len(toy_type)-1:
        while (toy_type[q] == toy_type[q+1]):
            del toy_type[q]
            del toy_type[q] #숫자항을 지우면 q+1자리 숫자가 q자리로 바뀜
            count=count+2
            q=0
            if len(toy_type)<=1: ##생각하기 어려움
                break 
        q= q+1
    answer = count
    
    return answer
  
  #주의사항
  #toy_type에 0이 포함되어있지 않을 수도 있다.
  #toy_type의 항의 개수가 1개 이하라면 멈춰야한다.
