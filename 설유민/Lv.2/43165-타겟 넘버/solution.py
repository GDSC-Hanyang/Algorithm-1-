def solution(numbers, target):
    tree = [0]
    for number in numbers:
        branch = []
        for leaf in tree:
            branch.append(leaf + number)
            branch.append(leaf - number)
        tree = branch
    return tree.count(target)