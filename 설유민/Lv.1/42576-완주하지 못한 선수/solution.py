def solution(participant, completion):
    sorted_participant = sorted(participant)
    sorted_completion = sorted(completion)
    for index in range(0, len(completion)):
        if sorted_participant[index] != sorted_completion[index]:
            return sorted_participant[index]
    return sorted_participant[-1]