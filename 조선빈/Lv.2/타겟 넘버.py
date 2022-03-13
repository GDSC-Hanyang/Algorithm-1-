def solution(numbers, target):
    answer = 0
    ex = [0]
    for i in numbers:
        example = []
        for j in ex:
            example.append(i+j)
            example.append(j-i)
        ex = example
    answer = ex.count(target)
    return answer
