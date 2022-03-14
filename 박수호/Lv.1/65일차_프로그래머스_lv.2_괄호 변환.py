def isRight(s):
    s = list(s)
    stack = []
    while s:
        a = s.pop(0)
        if stack and stack[-1] == "(" and a == ")":
            stack.pop()
        else:
            stack.append(a)
    return False if stack else True

def isBalance(s):
    return s.count("(") == s.count(")")

def slice(s):
    for i in range(2, len(s)+1, 2):
        if isBalance(s[:i]) and isBalance(s[i:]):
            return s[:i], s[i:]

def change(u):
    u = u[1:-1]
    tmp = ""
    for i in u:
        if i == "(":
            tmp += ")"
        else:
            tmp += "("
    return tmp

def solution(p):
    if not p: return p
    if isRight(p): return p
    u, v = slice(p)
    if isRight(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + change(u)