def solution(n, lost, reserve):
    tmp = [1 for _ in range(n)]
    for i in lost:
        tmp[i-1] -= 1
    for i in reserve:
        tmp[i-1] += 1
    answer = 0
    for i in range(len(tmp)):
        if tmp[i] == 1 or tmp[i] == 2: # 해당 학생이 1벌 또는 2벌일 때
            answer += 1
        elif tmp[i] == 0: # 해당 학생이 옷이 없을 때
            if i == 0:
                if tmp[1] == 2: # 처음 학생일 때 뒤에 학생이 여벌 있을 때
                    answer += 1
                else:
                    continue
            elif i == len(tmp)-1:
                if tmp[i-1] == 2: # 마지막 학생일 때 앞의 학생이 여벌 있을 때
                    answer += 1
                else:
                    continue
            else: # 중간 학생일 때
                if tmp[i-1] == 2: # 앞에 학생이 여벌 있을 때
                    tmp[i-1] = 1
                    tmp[i] = 1
                    answer += 1
                elif tmp[i+1] == 2: #뒤에 학생이 여벌 있을 떄
                    tmp[i + 1] = 1
                    tmp[i] = 1
                    answer += 1
    return answer