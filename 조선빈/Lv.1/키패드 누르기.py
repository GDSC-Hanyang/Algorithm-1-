def solution(numbers, hand):
    l = 10
    r = 11
    answer = ""
    distance = [[0,4,3,4,3,2,3,2,1,2],
               [4,0,1,2,1,2,3,2,3,4],
               [3,1,0,1,2,1,2,3,2,3],
               [4,2,1,0,3,2,1,4,3,2],
               [3,1,2,3,0,1,2,1,2,3],
               [2,2,1,2,1,0,1,2,1,2],
               [3,3,2,1,2,1,0,3,2,1],
               [2,2,3,4,1,2,3,0,1,2],
               [1,3,2,3,2,1,2,1,0,1],
               [2,4,3,2,3,2,1,2,1,0],
               [1,3,4,5,2,3,4,1,2,3],
               [1,5,4,3,4,3,2,3,2,1]]
    for i in numbers:
        if i in [1, 4, 7]:
            l = i
            answer += "L"
        elif i in [3, 6, 9]:
            r = i
            answer += "R"
        else:
            if distance[l][i] < distance[r][i]:
                l = i
                answer += "L"
            elif distance[l][i] > distance[r][i]:
                r = i
                answer += "R"
            elif hand == "left":
                l = i
                answer += "L"
            else:
                r = i
                answer += "R"
    return answer
