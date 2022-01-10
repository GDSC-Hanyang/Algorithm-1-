def solution(participant, completion):
    completion.append("")
    participant.sort(reverse=True)
    completion.sort(reverse=True)
    for i, j in list(zip(participant, completion)):
        if i != j:
            return i