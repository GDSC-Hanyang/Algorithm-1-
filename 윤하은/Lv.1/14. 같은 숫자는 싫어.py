def solution(arr):
    i = 0
    answer = [arr[0]]

    while i < len(arr)-1:
        k = answer[len(answer)-1]
        if k != arr[i+1]:
            answer.append(arr[i+1])
        i += 1

    return answer