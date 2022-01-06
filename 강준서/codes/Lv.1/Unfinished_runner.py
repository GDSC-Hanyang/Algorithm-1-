from collections import Counter

def solution(participant, completion):
    Retire = Counter(participant)
    Retire.subtract(Counter(completion))
    return sorted(Retire.elements())[0]
  
