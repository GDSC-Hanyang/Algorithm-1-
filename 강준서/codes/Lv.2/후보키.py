from itertools import combinations

def solution(relation):
    cand_keys = []  # 후보키
    cand = []  # 후보키 쌍 경우의수
    answer = 0

    # 후보키 모든 경우의 수 생성
    ### 비스마스킹을 활용하면 메모리를 훨씬 절약할 수 있을 것 같은데, 아직 익숙하지 않음...
    for i in range(1,len(relation[0])+1):
        for num in combinations(range(len(relation[0])),i): cand.append(num)

    for keys in cand:
        # 최소성 확인
        flag = False
        for key_set in cand_keys:
            if key_set.issubset(keys):
                flag = True
                break
        if flag: continue

        # 유일성 확인
        temp = []        
        for i in relation: temp.append('/'.join([i[int(key)] for key in keys]))

        if len(temp)==len(set(temp)): 
            cand_keys.append(set(keys))
            answer+=1

    return answer
  
