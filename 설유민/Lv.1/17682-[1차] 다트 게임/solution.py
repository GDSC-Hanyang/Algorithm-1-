import re

def solution(dartResult):
    results = re.findall(r'\d+[SDT][\*\#]?', dartResult)
    scores = [int(re.search(r'\d+', result).group()) for result in results]
    bonuses = [re.search(r'[SDT]', result).group() if re.search(r'[SDT]', result) != None else '' for result in results]
    options = [re.search(r'[\*\#]', result).group() if re.search(r'[\*\#]', result) != None else '' for result in results]
    for index in range(0, len(scores)):
        if bonuses[index] == 'D':
            scores[index] **= 2
        elif bonuses[index] == 'T':
            scores[index] **= 3
        if options[index] == '*':
            scores[index] *= 2
            if index > 0:
                scores[index - 1] *= 2
        elif options[index] == '#':
            scores[index] *= (-1)
    return sum(scores)
