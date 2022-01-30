def solution(answers):
    ans1 = [1,2,3,4,5]
    ans2 = [2,1,2,3,2,4,2,5]
    ans3 = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0,0,0]
    answer = []
    
    for i in range(len(answers)):
        if answers[i] == ans1[(i%5)]:
            cnt[0] += 1
        if answers[i] == ans2[(i%8)]:
            cnt[1] += 1
        if answers[i] == ans3[(i%10)]:
            cnt[2] += 1
    for i in range(3):
        if cnt[i] == max(cnt):
            answer.append(i+1)
    
    return answer
