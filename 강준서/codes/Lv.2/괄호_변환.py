def solution(p):
    # function
    def IsCorrect(s):
        flag = 0
        idx = 0
        while flag>=0 and idx<len(s):
            if s[idx]=='(': flag += 1
            else: flag -= 1
            idx += 1
        return False if flag<0 else True

    # Step 1
    if not p : return ''

    # Step 2
    flag = 1 if p[0]=='(' else -1
    idx = 1
    while flag:
        if p[idx]=='(': flag += 1
        else: flag -=1
        idx += 1

    u, v = p[:idx], p[idx:]

    # Step 3
    if IsCorrect(u): return u + solution(v)

    # Step 4
    else: return '(' + solution(v) + ')' + ''.join(['(' if x==')' else ')' for x in u[1:-1]])
