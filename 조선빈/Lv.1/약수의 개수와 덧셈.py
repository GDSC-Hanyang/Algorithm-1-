def measure(num):
    cnt = 0
    for i in range(1, num+1):
        if num%i == 0:
            cnt += 1
    return cnt

def num_measure(m_left,left):
    answer = 0
    if m_left%2 == 0:
        answer = answer + left
    else:
        answer = answer - left
    return answer

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        measure(i)
        answer = answer + num_measure(measure(i),i)
    return answer
