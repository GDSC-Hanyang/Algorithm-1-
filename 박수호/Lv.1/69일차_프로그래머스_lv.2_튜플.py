def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s.sort(key= lambda x : len(x))
    for i in s:
        a = set(map(int, i.split(",")))
        answer += list(a - set(answer))
    return answer