def solution(new_id):
    # 1. 대문자 소문자 변환
    answer = new_id.lower()
    print(answer)
    # 2. 이상한문자 모두 제거
    for i in answer:
        if i not in ('qwertyuiopasdfghjklzxcvbnm1234567890-_.'):
            answer = answer.replace(i, "")
    print(answer)
    # 3. ..을 . 으로
    while ".." in answer:
        answer = answer.replace("..", ".")
    print(answer)
    # 4. .이 처음이나 끝에 잇다면
    if answer == ".":
        answer = ""
    if answer != "" and answer[0] == ".":
        answer = answer[1:]
    if answer != "" and answer[-1] == ".":
        answer = answer[:-1]
    print(answer)
    # 5. 공백 처리
    if answer == "":
        answer = "a"
    # 6. 16자 이상->처음 15
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == ".":
        answer = answer[:-1]
    # 7. 2이하면 마지막문자 반복
    while len(answer) <= 2:
        answer += answer[-1]

    return answer
