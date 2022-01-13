def solution(array, commands): 
    answer = []
    for arr in commands:
        answer.append(sorted([array[i] for i in range(arr[0] - 1, arr[1])])[arr[2]-1])
    return answer