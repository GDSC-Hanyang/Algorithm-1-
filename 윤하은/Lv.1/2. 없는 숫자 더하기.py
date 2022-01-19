#없는 숫자 더하기

import random
    

def solution(numbers):
    answer = 0
    print('numbers', numbers)
    for i in range(0,10):
        print('i', i)
        if i not in numbers:
            answer = answer + i
            print('ans', answer)
    return answer