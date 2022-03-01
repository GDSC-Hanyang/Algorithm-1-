def solution(x):
    return False if x % eval("+".join(str(x))) else True
