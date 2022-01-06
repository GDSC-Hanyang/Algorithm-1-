import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # heap 생성

    while(len(scoville)>1):
        min_ = heapq.heappop(scoville) # 최소값을 min_에 pop
        if(min_ >= K): return answer # 종료 조건 : 최소값이 K 이상

        min_sec = heapq.heappop(scoville) # 두번째 최소값을 min_sec에 pop
        heapq.heappush(scoville,(min_+2*min_sec)) # 섞은 음식을 다시 push
        answer += 1

    # 마지막까지 조건을 달성 못한 case
    last = heapq.heappop(scoville)
    if(last>=K): return answer
    else: return -1
    
