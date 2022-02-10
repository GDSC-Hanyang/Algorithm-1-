def solution(s):
    sets = sorted(s[2:-2].split("},{"), key = lambda x: len(x))
    ans = []
    for i in range(len(sets)): sets[i]=sets[i].split(',')

    for i in range(len(sets)):
        temp = sets[i][0]
        ans.append(int(temp))
        for j in range(i,len(sets)): sets[j].remove(temp)

    return ans
