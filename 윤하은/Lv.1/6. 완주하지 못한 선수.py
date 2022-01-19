def solution(participant, completion):
    ptHash = dict()
    
    #hash key값에 대한 value 추가
    for i in participant:
        if i not in ptHash:
            ptHash[i] = 1
        else:
            ptHash[i] += 1
            
    #completion과 비교하여 value 조정
    for i in completion:
        if i in ptHash:
            ptHash[i] -= 1
    
    #0이상인 value에 대한 Key값 도출
    for key, value in ptHash.items():
        if value > 0: answer = key
    return answer