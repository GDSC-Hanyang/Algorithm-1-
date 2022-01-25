def solution(sizes):
    minSize = []
    maxSize = []
    for i in range(len(sizes)) : minSize.append(min(sizes[i]))
    for j in range(len(sizes)) : maxSize.append(max(sizes[j]))
    answer = max(minSize) * max(maxSize)
    return answer