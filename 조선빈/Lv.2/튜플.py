def solution(s):
    answer = []
    lists = sorted([s.split(',') for s in s[2:-2].split('},{')], key=len)
    for i in lists:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
                break
    return answer
