def solution(s, n):
    answer = ''
    for c in s:
        if 65 <= ord(c) <= 90:
            if 65 <= ord(c) + n <= 90:
                answer += chr(ord(c) + n)
            else:
                answer += chr(ord(c) + n - 26)
        elif 97 <= ord(c) <= 122:
            if 97 <= ord(c) + n <= 122:
                answer += chr(ord(c) + n)
            else:
                answer += chr(ord(c) + n - 26)
        else:
            answer += c
    return answer