def WhatDay(b):
    if b%7 == 0:
        answer = 'THU'
    if b%7 == 1:
        answer = 'FRI'
    if b%7 == 2:
        answer = 'SAT'
    if b%7 == 3:
        answer = 'SUN'
    if b%7 == 4:
        answer = 'MON'
    if b%7 == 5:
        answer = 'TUE'
    if b%7 == 6:
        answer = 'WED'
    return answer
def solution(a, b):
    answer = ''
    
    Jan = list(range(1,32))
    Feb = list(range(1,30))
    Mar = Jan.copy()
    Apr = list(range(1,31))
    May = Jan.copy()
    Jun = Apr.copy()
    Jul = Jan.copy()
    Aug = Jan.copy()
    Sep = Apr.copy()
    Oct = Jan.copy()
    Nov = Apr.copy()
    Dec = Jan.copy()
    #Month = [Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec]
    
    if a == 1:
        date = []
    if a == 2:
        date = Jan
    if a == 3:
        date = Jan + Feb
    if a == 4:
        date = Jan + Feb + Mar
    if a == 5:
        date = Jan + Feb + Mar + Apr
    if a == 6:
        date = Jan + Feb + Mar + Apr + May
    if a == 7:
        date = Jan + Feb + Mar + Apr + May + Jun
    if a == 8:
        date = Jan + Feb + Mar + Apr + May + Jun + Jul
    if a == 9:
        date = Jan + Feb + Mar + Apr + May + Jun + Jul + Aug
    if a == 10:
        date = Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep
    if a == 11:
        date = Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep + Oct
    if a == 12:
        date = Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep + Oct + Nov
    answer = WhatDay(len(date)+b)
   
    return answer
