def solution(new_id):
    answer = ''
    new=[]
    new=list(new_id)
    Large=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    i=0
    while i<len(new):
        j=0
        while j<len(Large):
            if new[i] == Large[j]:
                new[i]=Small[j]
            j+=1
        i+=1
    print(new)
    Special=['~','!','@','#','$','%','^','&','*','(',')','=','+','[','{',']','}',':','?',',','<','>','/',';']
    j=0
    while j<len(new):
        if new[j] in Special:
            del new[j]
        else:
            j+=1
    print(new)
    new_i=''.join(new)
    print(new_i)
    while '..' in new_i:
        new_i = new_i.replace('..','.')
    print(new_i)
    new=list(new_i)
    print(new)
    while new[0]=='.':
        del new[0]
        if new==[]:
            new=['a']
    if len(new)>=16:
        k=15
        while k<len(new):
            del new[k]
    print(new)
    while new[len(new)-1]=='.':
        del new[len(new)-1]
    if len(new)<=2:
        while len(new)<3:
            new.append(new[len(new)-1])
    answer=''.join(new)
    print(new)
    return answer
