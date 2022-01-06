def solution(numbers, hand):
    answer = ''
    left = (3,0)
    right = (3,2)
    _dict = {
            1:(0,0),
            2:(0,1),
            3:(0,2),
            4:(1,0),
            5:(1,1),
            6:(1,2),
            7:(2,0),
            8:(2,1),
            9:(2,2),
            0:(3,1)
            }

    for i in numbers:
        if (i==1 or i==4 or i==7):
            answer+='L'
            left=_dict[i]
        elif (i==3 or i==6 or i==9):
            answer+='R'
            right=_dict[i]
        else:
            current = _dict[i]
            ldistance = abs(current[0]-left[0]) + abs(current[1]-left[1])
            rdistance = abs(current[0]-right[0]) + abs(current[1]-right[1])
            if(ldistance>rdistance):
                answer+='R'
                right=current
            elif(ldistance<rdistance):
                answer+='L'
                left=current
            else:
                if(hand=='right'):
                    answer+='R'
                    right=current
                else:
                    answer+='L'
                    left=current

    return answer
