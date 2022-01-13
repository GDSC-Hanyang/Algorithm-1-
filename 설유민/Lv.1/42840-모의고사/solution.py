def solution(answers):
    count = [0, 0, 0]
    first_pattern = [1, 2, 3, 4, 5]
    second_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    third_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for index in range(0, len(answers)):
        if answers[index] == first_pattern[index % 5]:
            count[0] += 1
        if answers[index] == second_pattern[index % 8]:
            count[1] += 1
        if answers[index] == third_pattern[index % 10]:
            count[2] += 1
    answer = [i + 1 for i in range(0, 3) if count[i] == max(count)]
    return answer
