import re

def solution(new_id):
    # 1
    answer = new_id.lower()

    # 2
    answer = re.sub("[^\w\-\_\.]", "", answer)

    # 3
    while answer.find("..") != -1:
        answer = re.sub("\.\.", ".", answer)

    # 4
    answer = answer.lstrip(".").rstrip(".")

    # 5
    if len(answer) == 0:
        answer = "a"

    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[14] == ".": answer = answer[:14]

    # 7
    while len(answer) <= 2:
        answer += answer[-1]

    return answer