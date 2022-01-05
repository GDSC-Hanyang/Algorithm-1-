special_characters = "~!@#$%^&*()=+[{]}:?,<>/"

def solution(new_id):
    new_id = new_id.lower() #1단계
    
    
    new_id = ''.join(x for x in new_id if x not in special_characters) #2단계   
    
    while True :
        if new_id.find("..") != -1 :
            new_id = new_id.replace('..', '.')
        else :
            break #3단계
    
    
    new_id = new_id.strip('.')#4단계
    
    if len(new_id) == 0 : new_id = "a"#5단계
    elif len(new_id) >= 16 :
        new_id = new_id[0:15]
        if new_id[0] == "." or new_id[-1] :
            new_id = new_id.strip('.') #6단계
    if len(new_id) <= 2 :
        new_id = list(new_id)
        while len(new_id) <= 2 :
            new_id.append(new_id[len(new_id)-1])#7단계
            
        new_id = "".join(new_id)
    
    return new_id