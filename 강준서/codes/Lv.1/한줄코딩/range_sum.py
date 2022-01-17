def solution(a, b): return sum(list(range(min(a,b),max(a,b)+1)))
# This solution is O(n), so it's not good.
# You can make it O(1) by using a bit math.
