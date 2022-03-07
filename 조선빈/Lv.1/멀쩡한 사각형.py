def solution(w,h):
    w1=w 
    h1=h
    while(w1!=h1):
        if w1>h1:
            w1-=h1
        else:   
            h1-=w1

    return w*h-(w+h-h1)
