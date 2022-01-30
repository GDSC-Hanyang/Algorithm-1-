def solution(s):
    answer = ''
    if len(s)%2 == 0:
        num1 = s[len(s)//2-1]
        num2 = s[len(s)//2]
        answer += num1
        answer += num2
    if len(s)%2 == 1:
        num = s[len(s)//2]
        answer += num
    return answer
