def solution(numbers, hand):
    answer = ''

    left = 10
    right = 12

    # 키패드의 각 칸을 좌표로 나타냄 (0~3, 0~2)
    coords = {}
    for num in range(1, 13):
        coords[num] = {'row': (num - 1) //3, 'col': (num - 1) % 3}
    
    sub_numbers = [11 if num == 0 else num for num in numbers]
    
    for num in sub_numbers:
        if num % 3 == 1:
            answer += 'L'
            left = num
        elif num % 3 == 0:
            answer += 'R'
            right = num
        else:
            left_dist = abs(coords[left]['row'] - coords[num]['row']) + abs(coords[left]['col'] - coords[num]['col'])
            right_dist = abs(coords[right]['row'] - coords[num]['row']) + abs(coords[right]['col'] - coords[num]['col'])
            print(f"left dist: {left_dist}, right dist: {right_dist}")
            if (left_dist < right_dist) or ((left_dist == right_dist) and (hand == "left")):
                answer += 'L'
                left = num
            elif (left_dist > right_dist) or ((left_dist == right_dist) and (hand == 'right')):
                answer += 'R'
                right = num
        print(f"left: {left}, right: {right}")
    return answer
