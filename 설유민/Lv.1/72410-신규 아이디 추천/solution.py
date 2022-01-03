import re

def solution(new_id):
    # 1단계: 모든 대문자를 대응되는 소문자로 치환
    answer = new_id.lower()

    # 2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    answer = re.sub(r'[^a-z0-9-_.]', '', answer)

    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while ".." in answer:
        answer = answer.replace("..", '.')

    # 4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거
    try:
        if answer[0] == '.':
            answer = answer[1:]
        if answer[-1] == '.':
            answer = answer[:-1]
    except:
        pass

    # 5단계:빈 문자열이라면, "a"를 대입
    if len(answer) == 0:
        answer = 'a'

    # 6단계: 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if len(answer) >= 16:
        answer = answer[0:15]

    # 7단계: 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임
    while len(answer) < 3:
        answer += answer[-1]
    
    # 6단계 이후 4단계 한 번 더 수행
    if answer[-1] == '.':
        answer = answer[:-1]

    return answer