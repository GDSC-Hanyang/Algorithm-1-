def solution(n):
    answer = ''
    while n > 0:
        answer += str(n % 3)
        n //= 3
    answer = list(answer.strip('0'))
    for index in range(0, len(answer)):
        answer[index] = int(answer[index]) * (3 ** (len(answer) - index - 1))
    answer = sum(answer)
    return answer