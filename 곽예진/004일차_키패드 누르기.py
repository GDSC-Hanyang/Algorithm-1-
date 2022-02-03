#키패드 누르기
#https://programmers.co.kr/learn/courses/30/lessons/67256

<1> for 반복문 활용


#키보드에서 *은 10으로 #은 11로 두었다.
#숫자 2,5,8,0을 뽑을 때 각 번호와의 거리를 미리 구해두어  decide 리스트로 두었다.
#이때, 숫자 0부터 9까지 숫자가 인덱스 숫자와 같도록 위치시켰다.
decide_2='310121232344'
decide_5='221210121233'
decide_8='132321210122'
decide_0='043432321211'

#2,5,8,0에 대한 경우를 합쳐 decide 딕셔너리로 두었다.
decide={2:decide_2,5:decide_5,8:decide_8,0:decide_0}

#이때numbers가 [ , , , , ,]형태로 주어진다.
#이 때문에 for 반목문에서 str(numbers)가 아니라 그냥 numbers로 해야한다.
##str(numbers)로 하면 ','도 인식하여 오류가 난다. 
def solution(numbers, hand):
    answer=''
    left_now=10
    right_now=11
    for i in numbers:
        if (i==1 or i==4 or i==7):
            usehand='L'
            left_now=int(i)
        elif (i==3 or i==6 or i==9):
            usehand='R'
            right_now=int(i)
        else:
            a= decide[i][left_now]
            b= decide[i][right_now]
            
            if  int(a) > int(b) :
                usehand='R'
                right_now=int(i)
            elif int(a) < int(b):
                usehand='L'
                left_now=int(i)
            else:
                if hand=='left':
                    usehand='L'
                    left_now=int(i)
                else:
                    usehand='R'
                    right_now=int(i)
        answer=answer +usehand
    return answer
#answer는 usehand들을 더한 식으로 생각한다.



---------------------------------------------------------------------------------------

##가정-2
#(만약 numbers가 숫가열이 아닌 그냥 숫자로 주어졌을 때)

decide_2='310121232344'
decide_5='221210121233'
decide_8='132321210122'
decide_0='043432321211'
decide={'2':decide_2,'5':decide_5,'8':decide_8,'0':decide_0}

def solution(numbers, hand):
    answer=''
    left_now=10
    right_now=11
    for i in str(numbers):
        if i=='1' or i=='4' or i=='7':
            usehand='L'
            left_now=int(i)
        elif i=='3' or i=='6' or i=='9':
            usehand='R'
            right_now=int(i)
        else:
            a= decide[i][left_now]
            b= decide[i][right_now]
            if  int(a) > int(b) :
                usehand='R'
                right_now=int(i)
            elif int(a) < int(b):
                usehand='L'
                left_now=int(i)
            else:
                if hand=='left':
                    usehand='L'
                    left_now=int(i)
                else:
                    usehand='R'
                    right_now=int(i)
        answer=answer+usehand
    return answer


--------------------------------------------------------------------------------------------------
