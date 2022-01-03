dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
       "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def solution(s):
    answer = ""
    tmp = ""
    for i in s:
        if i.isalpha(): # 문자면
            tmp += i
        else : # 숫자면
            answer += i
        if tmp in dic.keys():
            answer += dic[tmp]
            tmp = ""
    answer = int(answer)
    return answer