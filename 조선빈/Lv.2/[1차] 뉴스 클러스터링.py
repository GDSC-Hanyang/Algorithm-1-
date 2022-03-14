from collections import Counter

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    str1_list = []
    str2_list = []

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_list.append(str1[i]+str1[i+1])
    for j in range(len(str2)-1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            str2_list.append(str2[j]+str2[j+1])

    cnt1 = Counter(str1_list)
    cnt2 = Counter(str2_list)
    inter = []
    union = cnt1
    inter = list((cnt1 & cnt2).elements())
    union = list((cnt1 | cnt2).elements())

    if len(union) == 0 and len(inter) == 0:
        answer = 65536
    else:
        answer = int(len(inter)/len(union) * 65536)
    return answer
