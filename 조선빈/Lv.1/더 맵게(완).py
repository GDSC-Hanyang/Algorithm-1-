import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville) #heap 생성
    answer = 0
    
    while True:
        first = hq.heappop(scoville) #최소를 빼는 명령어 in heapq
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
