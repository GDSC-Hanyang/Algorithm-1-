def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        plus = []
        for j in range(len(arr1[i])):
            plus.append(arr1[i][j]+arr2[i][j])
        answer.append(plus)
    return answer
