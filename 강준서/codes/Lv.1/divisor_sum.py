def solution(n):
    answer = 0
    itr = 1

    while(True):
        if(itr>n/itr): break
        if(n%itr==0):
            if(n/itr == itr): answer+=itr
            else: answer+=(n/itr+itr)
        itr+=1

    return answer
