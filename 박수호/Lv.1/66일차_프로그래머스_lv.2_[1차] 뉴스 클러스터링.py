import math
def solution(str1, str2):
    answer = 0
    tmp1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    tmp2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if not tmp1 and not tmp2:
        return 65536

    if len(tmp1) < len(tmp2):
        a, b = tmp1[:], tmp2[:]
    else:
        a, b = tmp2[:], tmp1[:]

    cnt = 0
    for i in a:
        tmp = b[:]
        for j in tmp:
            if i == j:
                cnt += 1
                b.remove(i)
                break
    return math.floor((cnt/(len(tmp1)+len(tmp2)-cnt))*65536)