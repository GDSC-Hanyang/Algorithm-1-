def solution(s, n):
    lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    answer = ''
    alpha = list(s)

    for i in range(len(alpha)) : 
        if alpha[i] in lower :
            answer += lower[(lower.index(alpha[i])+n)%26]
        elif alpha[i] in upper :
            answer += upper[(upper.index(alpha[i])+n)%26]
        elif alpha[i] == ' ' :
            answer += ' '

    return answer