def solution(s, n):
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low = up.lower()
    answer = ''

    for i in s:
        if i == ' ': answer+=' '
        elif i in up: answer+=up[(up.index(i)+n)%26]
        else: answer+=low[(low.index(i)+n)%26]
  
    return answer
