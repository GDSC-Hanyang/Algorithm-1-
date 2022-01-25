def solution(a, b):
    day_wk = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return day_wk[(sum(days[:a - 1]) + b) % 7]