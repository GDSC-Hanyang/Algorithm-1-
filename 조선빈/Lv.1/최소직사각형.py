def solution(sizes):
    w = 0
    h = 0
    for xy in sizes:
        x = min(xy)
        y = max(xy)
        if w * h == 0 :
            w = x
            h = y
        else :
            w = max(w, x)
            h = max(h, y)
    answer = w * h
    return answer
