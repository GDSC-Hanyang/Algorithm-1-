def solution(sizes): #[[60, 50], [30, 70], [60, 30], [80, 40]]
    return max(map(lambda size : max(size), [size for size in sizes]))*max(map(lambda size : min(size), [size for size in sizes]))