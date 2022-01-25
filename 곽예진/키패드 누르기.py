decide_2='310121232344'
decide_5='221210121233'
decide_8='132321210122'
decide_0='043432321211'
decide={'2':decide_2,'5':decide_5,'8':decide_8,'0':decide_0}

def solution(numbers, hand):

    left_now='10'
    right_now='11'
    for i in str(numbers):
        if i=='1' or i=='4' or i=='7':
            usehand='L'
            left_now=i
        elif i=='3' or i=='6' or i=='9':
            usehand='R'
            right_now=i
        else:
            if decide[i][left_now] > decide[i][right_now]:
                usehand='R'
                right_now=i
            elif int(decide[i][left_now]) < int(decide[i][right_now]):
                usehand='L'
                left_now=i
            else:
                if hand=='left':
                    usehand='L'
                    left_now=i
                else:
                    usehand='R'
                    right_now=i
        answer = usehand
    return answer
