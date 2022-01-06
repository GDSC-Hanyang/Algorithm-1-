def solution(s):
    answer = ''
    words = s.split(" ")
    for idx, i in enumerate(words):
        for j in range(0,len(i),2):
            answer+=i[j].upper()
            if(j+1 == len(i)): break
            answer+=i[j+1].lower()
        if(idx!=len(words)-1):answer+=' '

    return answer
