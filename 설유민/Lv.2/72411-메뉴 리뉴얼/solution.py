from itertools import combinations
def solution(orders, course):
    answer = []
    orders = [sorted(order) for order in orders]
    for number in course:
        options = [''.join(tuple) for order in orders for tuple in combinations(order, number)]
        if len(options) > 0:
            times_selected = options.count(max(options, key=options.count))
            if times_selected > 1:
                answer.extend([option for option in options if options.count(option) == times_selected])
    return sorted(set(answer))