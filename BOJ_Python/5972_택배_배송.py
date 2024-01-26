import sys; input = sys.stdin.readline
import heapq

def dijkstra():
    W = [987654321] * (N+1)
    heap = [[0, 1]]
    
    while heap:
        dist, v = heapq.heappop(heap)
        if W[v] > dist:
            W[v] = dist
            for c, w in adj_l[v]:
                heapq.heappush(heap, [dist+c, w])

    return W[N]


N, M = map(int, input().split())
adj_l = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    adj_l[A].append([C, B])
    adj_l[B].append([C, A])

print(dijkstra())