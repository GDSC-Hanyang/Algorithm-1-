def solution(n):
    n_list = list(map(int,str(n)))
    n_list.sort(reverse = True)
    answer = ''.join(map(str,n_list))
    return int(answer)
