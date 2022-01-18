def solution(n, lost, reserve):
    lost_without_rez = sorted(list(set(lost) - set(reserve)))
    reserve_without_loss = sorted(list(set(reserve) - set(lost)))
    
    pairs = {}
    
    for lost_stu in lost_without_rez:
        for reserve_stu in reserve_without_loss:
            if ((lost_stu - reserve_stu) == -1 or (lost_stu - reserve_stu) == 1):
                pairs[reserve_stu] = lost_stu
    answer = n - len(lost_without_rez) + len(set(pairs))
    if answer > n:
        answer = n
    return answer