from datetime import datetime
import re

def solution(a, b):
    nowStr = "2016년 " + str(a) + "월 " +str(b) + "일"
    nowDate = datetime.strptime(nowStr, "%Y년 %m월 %d일")
    fstDate = datetime.strptime("2015년 12월 31일", "%Y년 %m월 %d일")
    days = str(nowDate - fstDate)[:-9]
    sevenDays = int(re.findall("\d+", days)[0]) % 7
    week = {
        1 : 'FRI',
        2 : 'SAT',
        3 : 'SUN',
        4 : 'MON',
        5 : 'TUE',
        6 : 'WED',
        0 : 'THU'
    }
    answer = week.get(sevenDays)
    return answer