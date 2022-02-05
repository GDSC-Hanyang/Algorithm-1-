def solution(s):
    answer = ''
    is_even = 1
    for i in range(0, len(s)):
        if is_even == 1:
            answer += s[i].upper()
            if s[i] != ' ':
                is_even = 0
        else:
            answer += s[i].lower()
            is_even = 1
    return answer