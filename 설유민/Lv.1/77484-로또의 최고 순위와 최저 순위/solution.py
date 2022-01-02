def solution(lottos: list, win_nums: list):
    n_matches = len(list(set(lottos) & set(win_nums)))
    n_zeros = lottos.count(0)
    rank = [6, 6, 5, 4, 3, 2, 1]
    answer = [rank[n_matches + n_zeros], rank[n_matches]]
    return answer