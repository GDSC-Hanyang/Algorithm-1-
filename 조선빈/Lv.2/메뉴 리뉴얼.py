from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        temp = []
        for order in orders:
            comb = combinations(sorted(order), i)
            temp += comb
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) !=1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
        answer = sorted(answer)
    return answer
