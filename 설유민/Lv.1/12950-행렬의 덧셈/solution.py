def solution(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(0, len(arr1[0]))] for i in range(0, len(arr1))]