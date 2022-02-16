def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            p = ord(s[i]) - ord('A') + n
            s[i] = chr(p % 26 + ord('A'))
        elif s[i].islower():
            p = ord(s[i]) - ord('a') + n
            s[i] = chr(p % 26 + ord('a'))
    answer = "".join(s)
    return answer
  
  
def solution(s, n):
    low = 'abcdefghijklmnopqrstuvwxyz'*2
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*2
    answer = ''
    for i in s:
        if i in up:
            answer += up[up.index(i)+n]
        elif i in low:
            answer += low[low.index(i)+n]
        else:
            answer += i
    return answer
