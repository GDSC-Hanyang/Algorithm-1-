def solution(numbers, hand):
    answer = ""
    left, right = 10, 12
    for i in numbers:
        if i == 0: i = 11
        if i in [1, 4, 7]: answer += "L"
        elif i in [3, 6, 9]: answer += "R"
        else:
            ldistance = abs(i-left-1)//3+1 if left in [1, 4, 7, 10] else abs(i-left)//3
            rdistance = abs(right-i-1)//3+1 if right in [3, 6, 9, 12] else abs(right-i)//3

            if ldistance < rdistance:
                answer += "L"
            elif ldistance > rdistance:
                answer += "R"
            else:
                answer += "L" if hand == "left" else "R"

        if answer[-1] == "L":
            left = i
        elif answer[-1] == "R":
            right = i
    return answer