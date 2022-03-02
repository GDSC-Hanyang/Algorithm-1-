from collections import defaultdict

def solution(id_list, report, k):
    report = set(report)
    report_dict = defaultdict(list)

    for log in report:
        temp = log.split()
        report_dict[temp[1]].append(temp[0])

    user_table = dict(zip(id_list,range(len(id_list))))
    answer = [0 for _ in range(len(id_list))]
    for user in report_dict:
        if len(report_dict[user])>=k:
            for reporter in report_dict[user]:
                answer[user_table[reporter]]+=1

    return answer
