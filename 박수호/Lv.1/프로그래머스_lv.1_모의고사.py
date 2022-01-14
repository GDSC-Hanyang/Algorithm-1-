def solution(answers):
    tmp = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    correct_list = []
    for i in tmp:
        cnt = 0
        correct = 0
        for j in answers:
            if cnt == len(i): cnt = 0
            if j == i[cnt]: correct += 1
            cnt += 1
        correct_list.append(correct)
    top = max(correct_list)
    answer = []
    for i in range(3):
        if top == correct_list[i]: answer.append(i+1)
    return answer