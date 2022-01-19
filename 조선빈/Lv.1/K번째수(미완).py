def solution(array, commands):
    answer = []
    
    for i in range(0,len(commands)):
        Arr = sorted(array[commands[i][0]:commands[i][1]])
        num = Arr[commands[i][2]]
        answer.append(num)


    return answer
