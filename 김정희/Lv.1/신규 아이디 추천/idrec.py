def solution(new_id):
    #1
    new=list(new_id) #문자열은 수정이 안된다 !!
    for c in new:
        if 65<=ord(c)<=90:
            n=ord(c)+32
            i=new.index(c)
            print(i)
            new[i]=chr(n)
    #2
    for c in new:
        if 97<=ord(c)<=122 || 0<=ord(c)<=9|| c in "-_.":
            pass
        else:
            new.remove(c)
    #3
    if ".." in new_id
    
    
    
    
    answer = ''.join(new)
    return answer
