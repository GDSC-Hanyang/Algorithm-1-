# 신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = {x: 0 for x in id_list}
    reporter = {x: set() for x in id_list}
    reported = {x: set() for x in id_list}
    for j in report:
        data = j.split(' ')
        reporter[data[0]].add(data[1])
        reported[data[1]].add(data[0])
    for i in id_list:
        if len(reported[i]) >= k:
            for j in reported[i]:
                answer[j] += 1
    answer = list(answer.values())
    return answer