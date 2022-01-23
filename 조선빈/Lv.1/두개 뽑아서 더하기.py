def solution(numbers):
    answer = []
    Number = sorted(numbers)
    for i in range(0,len(Number)-1):
        for j in range(i+1,len(Number)):
            answer.append(Number[i]+Number[j])
    result = list(set(answer))
    return sorted(result)
