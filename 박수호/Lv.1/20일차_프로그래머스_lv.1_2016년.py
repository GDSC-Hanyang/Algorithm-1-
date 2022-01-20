def solution(a, b):
    day = b
    while a > 1:
        if a == 3: day += 29
        elif a == 2 or a == 4 or a == 6 or a == 8 or a == 9 or a == 11:
            day += 31
        elif a == 5 or a == 7 or a == 10 or a == 12:
            day += 30
        a -= 1
    day -= 1
    week = day % 7
    answer = 'FRI' if week == 0 else 'SAT' if week == 1 else 'SUN' if week == 2 else 'MON' if week == 3 else 'TUE' if week == 4 else 'WED' if week == 5 else 'THU'
    return answer
