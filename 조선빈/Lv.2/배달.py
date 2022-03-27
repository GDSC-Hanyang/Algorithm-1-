import heapq

def dijkstra(dis, adj):
    heap = []
    heapq.heappush(heap,[0,1])
    
    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in adj[node]:
            if cost + c < dis[n]:
                dis[n] = cost + c
                heapq.heappush(heap, [cost + c, n])
                
def solution(N, road, K):
    answer = 0
    inf = float('inf')
    dis = [inf] * (N+1)
    dis[1] = 0
    adj = [[] for _ in range(N+1)]
    for r in road:
        adj[r[0]].append([r[2], r[1]])
        adj[r[1]].append([r[2], r[0]])
    dijkstra(dis, adj)
    answer = len([x for x in dis if x <= K])
    return answer
