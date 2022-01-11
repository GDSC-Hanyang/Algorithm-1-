def solution(s):
    answer = s
    # 반복이 된다 -> 이걸 다 손으로 작성할 게 아니라 반복되는 대상에 대한 따로 자료구조를 만들어서
    # 그거에 대해 반복을 시킨다 !!!
    num = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
           "eight": "8", "nine": "9"}
    # !!!! 0,1,2 이걸 따로 저장햇는데, 인덱스가 그대로 1,2,3이니까 그냥 인덱스 숫자 그대로 쓸 수도 잇겟다 !!

    for k, v in num.items():
        print(answer)
        answer = answer.replace(k, v)  # replace의 두 아규먼트는 무조건 string
    answer = int(answer)

    return answer