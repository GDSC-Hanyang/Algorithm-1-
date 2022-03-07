def solution(n):
    answer = ''
    tmp = ''
    
    if n % 3 == 1 :
        tmp = '1'
        
    elif n % 3 == 2 :
        tmp = '2'
        
    elif n % 3 == 0 :
        tmp = '4'
    
    if n % 3 == 0 : tmp = str(n//3 -1) + tmp
    else : tmp = str(n//3) + tmp
        
    
    return tmp.strip('0')