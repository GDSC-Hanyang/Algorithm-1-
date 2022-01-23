def solution(n, arr1, arr2):
    return [f'{(arr1[i] | arr2[i]):0{n}b}'.replace('1', '#').replace('0', ' ') for i in range(0, n)]