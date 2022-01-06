def solution(numbers):
    answer = 0
    for i in "123456789":
        if int(i) not in numbers:
            answer+=int(i)
    return answer
