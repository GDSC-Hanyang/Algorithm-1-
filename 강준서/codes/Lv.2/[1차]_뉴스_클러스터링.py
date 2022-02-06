from collections import Counter
def solution(str1, str2):
    answer = 65536

    L1, L2 = [], []
    for i in range(len(str1)-1): 
        if not str1[i:i+2].isalpha(): continue
        L1.append(str1[i:i+2].upper())
    for i in range(len(str2)-1): 
        if not str2[i:i+2].isalpha(): continue
        L2.append(str2[i:i+2].upper())

    C1, C2 = Counter(L1), Counter(L2)
    # Python 3.10 부터는 Counter.total()이라는 함수가 생겨서 이를 사용하면 된다.
    # 아직 프로그래머스의 컴파일 환경이 3.10 미만의 버전인듯 함.
    union, intersect = len(list((C1 | C2).elements())), len(list((C1 & C2).elements()))

    if not union: return answer
    return int(answer/union*intersect)
