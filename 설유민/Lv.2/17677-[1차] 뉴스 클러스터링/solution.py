import re
def solution(str1, str2):
    # 대문자와 소문자 차이를 무시하기 위해 모든 글자를 소문자로 변환
    str1, str2 = str1.lower(), str2.lower()
    
    # 다중집합을 구성하기 위한 변수 설정
    A = [] # str1의 다중집합
    B = [] # str2의 다중집합
    REGEX = r'[^a-z]' # 영문 소문자를 제외한 나머지 글자
    
    # 영문 소문자가 아닌 문자가 포함된 글자쌍을 버리고 다중집합 구성
    for index in range(0, len(str1) - 1):
        element = str1[index] + str1[index + 1]
        if re.findall(REGEX, element) == []:
            A.append(element)
    
    for index in range(0, len(str2) - 1):
        element = str2[index] + str2[index + 1]
        if re.findall(REGEX, element) == []:
            B.append(element)
    
    # 집합 A와 B가 모두 공집합인 경우 조건에 따라 65536을 return
    if len(A) == 0 and len(B) == 0:
        return 65536
    
    # 집합 A가 공집합인 경우 나눗셈의 법칙에 따라 0을 return
    if len(A) == 0 and len(B) != 0:
        return 0
    
    # 한 집합 내에 중복되는 원소가 있는지 판단
    duplicate = False # 중복되는 원소가 있는 경우 True, 그렇지 않은 경우 False
    count_A = dict() # 집합 A의 원소를 key, 등장 횟수를 value로 하는 dictionary
    count_B = dict() # 집합 B의 원소를 key, 등장 횟수를 value로 하는 dictionary
    
    for element in A:
        try:
            count_A[element] += 1
            duplicate = True
        except:
            count_A[element] = 1
            
    for element in B:
        try:
            count_B[element] += 1
            duplicate = True
        except:
            count_B[element] = 1
    
    # 중복되는 원소가 존재하지 않는 경우, 일반적인 집합의 연산의 정의를 따라 계산
    if duplicate == False:
        A, B = set(A), set(B)
        return int(len(A & B) / len(A | B) * 65536)
    
    # 중복되는 원소가 존재하는 경우, 다중집합의 정의에 맞는 교집합과 합집합 생성
    if duplicate == True:
        interception = dict()
        union = count_A.copy()
        
        for key in count_A.keys():
            if key in count_B.keys():
                interception[key] = count_A[key]
            union[key] = count_A[key]
            
        for key in count_B.keys():
            if key in count_A.keys():
                interception[key] = min(interception[key], count_B[key])
            try:
                union[key] = max(union[key], count_B[key])
            except: # 합집합 union에 해당 key가 없는 경우
                union[key] = count_B[key]
        
        return int(sum(interception.values()) / sum(union.values()) * 65536)