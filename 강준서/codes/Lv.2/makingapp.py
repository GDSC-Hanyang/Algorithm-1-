def solution(progresses, speeds):
    answer = []
    works = len(progresses)
    finished = 0
    stack = []

    while(finished < works):
        for i in range(works):
            progresses[i] += speeds[i]
            if(progresses[i]>=100):
                stack.append(i)
                progresses[i]=-1e9

        today = 0
        while(finished in stack):
            today +=1
            finished +=1

        if(today != 0): answer.append(today)

    return answer
  
