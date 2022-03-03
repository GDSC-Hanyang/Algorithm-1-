def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def solution(w, h):
    return w * h - (w + h - gcd(w, h))