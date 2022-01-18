def solution(numbers):
    answer=0
    for i in range(10):
        if i not in numbers:
            answer+=i
    return answer

# 45-sum(numbers) 이렇게하면 바로풀림 짜증남 ............~~