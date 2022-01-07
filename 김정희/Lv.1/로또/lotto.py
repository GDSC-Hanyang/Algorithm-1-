def check(n):
    if n == 6:
        return 1
    elif n == 5:
        return 2
    elif n == 4:
        return 3
    elif n == 3:
        return 4
    elif n == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    remain = 6
    for k in lottos:
        if k in win_nums:
            remain -= 1
    correct = 6 - remain

    zero = lottos.count(0)

    if zero >= remain:
        best = correct + remain
    else:
        best = zero + correct

    answer = [check(best), check(correct)]
    return answer


print(solution([1, 2, 0, 0, 5, 6], [5, 6, 7, 8, 9, 10]))