from itertools import product
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    bitmap = list(product((True, False), repeat=4))
    usermap = defaultdict(list)

    # 유저 해시테이블 생성
    for i in info: 
        user = i.split()
        for bit in bitmap:
            user_key = '/'.join([user[idx] if bit[idx] else '-' for idx in range(4)])
            usermap[user_key].append(int(user[4]))

    for i in usermap: usermap[i].sort() # 이분 탐색을 위한 정렬

    # 쿼리 파싱 후 해시테이블에서 목표 점수보다 높은 사람의 수 계산
    for i in query:
        query_key, target_score = '/'.join(i.split(' and ')).split()
        answer.append(len(usermap[query_key])-bisect_left(usermap[query_key],int(target_score)))

    return answer

### 시간복잡도

# i : 50000, q : 100000

# 해시태이블 생성 : O(i) * bitmap => 50000 * 16
# 정렬 : O(ilogi) => 50000 * 15.6 
# 쿼리 파싱 : O(q*(split+logq)) => 100000 * (5 + 16.6)

# 총 연산 수는 약 374만이고 join 함수까지 고려해도, 파이썬은 초당 2000만회의 연산이 가능하므로 충분히 통과 가능할듯 하다.
