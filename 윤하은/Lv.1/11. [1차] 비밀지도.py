def solution(n, arr1, arr2):
    new = []
    answer = []
    ans = ''

    for i in range(0,n) :
        new.append((bin(arr1[i] | arr2[i]))[2:])
    print(new)

    for j in new :
        while len(j) < n:
            j = '0' + j
        print(j)
        for k in range(0,n):
            if list(j)[k] == '1': ans = ans + '#'
            else: ans = ans + ' '
        answer.append(ans)
        ans = ''