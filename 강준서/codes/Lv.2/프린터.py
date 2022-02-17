def solution(priorities, location):
    answer = 0
    pr = list(enumerate(priorities))

    while pr:
        length, max_pr = len(pr), max(pr,key = lambda x : x[1])[1]
        for i in range(length):
            name, priority = pr.pop(0)
            if priority < max_pr: pr.append((name,priority))
            else:
                answer +=1
                if pr: max_pr = max(pr,key = lambda x : x[1])[1]
                if name == location: return answer
                
