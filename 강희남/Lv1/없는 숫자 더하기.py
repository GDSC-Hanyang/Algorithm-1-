def solution(numbers):
    answer = 45
    for i in range(0,9+1) :
        if numbers.count(i) : answer-=i
    return answer