def solution(sizes):
    max_max = 0
    min_max = 0

    for i in sizes:
        max_max = max(max_max, max(i))
        min_max = max(min_max, min(i))

    return max_max * min_max
