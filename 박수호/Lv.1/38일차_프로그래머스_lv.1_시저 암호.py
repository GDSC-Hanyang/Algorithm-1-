def solution(s, n):
    answer = ''
    for i in s:
        if i.islower():
            answer += chr(((ord(i)+n)%97)%26+97)
        elif i.isupper():
            answer += chr(((ord(i)+n)%65)%26+65)
        else:
            answer += " "
    return answer