def solution(sizes):
    sizes = [sorted(sizes[i]) for i in range(0, len(sizes))]
    return max([sizes[i][0] for i in range(0, len(sizes))]) * max([sizes[i][1] for i in range(0, len(sizes))])