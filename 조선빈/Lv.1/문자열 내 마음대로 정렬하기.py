def solution(strings, n):
    answer = []
    Str = []
    for i in range(len(strings)):
        Str.append(strings[i][n]+strings[i])
    print(Str)
    Str.sort()
    for j in range(len(Str)):
        answer.append(Str[j][1:])
    return answer
