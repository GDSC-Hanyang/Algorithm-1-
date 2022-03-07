def solution(id_list, report, k):
    #중복 제거 (동일한 유저에 대한 신고 횟수는 1회로 처리)
    new_report = []
    for v in report:
        if v not in new_report:
            new_report.append(v)
    reporting = []
    reported = []
    number = []
    answer = []
    #answer 리스트에 number(혹은 id_list)의 길이와 동일하도록 원소 0 넣어주기
    for s in range(0,len(id_list)):
        answer.append(0)
        
    #신고한 사람과 신고당한 사람을 각각 reporting과 reported 리스트에 담기
    for i in range(0,len(new_report)):
        reporting.append(new_report[i].split(" ")[0])
        reported.append(new_report[i].split(" ")[1])
        
    #신고당한 횟수 세서 id_list 순으로 number 리스트에 담기
    for j in range(0,len(id_list)):
        idx = j
        char = id_list[j]
        cnt = reported.count(char)
        number.append(cnt)
    #k가 신고당한 횟수와 같거나 더 크면 answer 리스트에 신고당한 횟수를 더해줌
    #신고당한 사람의 인덱스와 신고한 사람의 인덱스가 같으므로 그 위치에 해당하는 사람의 id_list에서의 인덱스를 찾기
    #answer는 id_list 순이므로 해당 위치에 1만큼 더해주기(처리 결과 메일 발송)
    for m in range(0,len(number)):
        if number[m]>=k:
            for n in range(0,len(reported)):
                if reported[n] == id_list[m]:
                    idx = id_list.index(reporting[n])
                    answer[idx] += 1       
    return answer


##변경 코드

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}
    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
