def solution(id_list, report, k):
    reporters = {id: set() for id in id_list}
    reported = {id: set() for id in id_list}
    banned = {id: 0 for id in id_list}
    for r in report:
        r = r.split(' ')
        reporters[r[0]].add(r[1])
        reported[r[1]].add(r[0])
    for r in reported.keys():
        if len(reported[r]) >= k:
            for n in reported[r]:
                banned[n] += 1
    return list(banned.values())