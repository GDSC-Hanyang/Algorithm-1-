def solution(n):
    if n<=3:
        answer = '124'[n-1]
    else:
        q,r = divmod(n-1,3)
        answer = solution(q) + '124'[r]
    return answer
