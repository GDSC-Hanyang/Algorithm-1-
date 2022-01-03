import re

def solution(s):
    table = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = s
    for letter in table:
        answer = re.sub(letter, str(table.index(letter)), answer)
    answer = int(answer)
    return answer