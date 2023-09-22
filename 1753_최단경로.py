import sys; input = sys.stdin.readline
import heapq

def dijkstra(start):
    heap = []
    W[start] = 0
    heapq.heappush(heap, (W[start], start))

    while heap:
        dist, v = heapq.heappop(heap)   # pop

        if dist <= W[v]:
            for w, weight in adj_l[v]:
                if W[w] > dist + weight:    # 갱신이 필요한 경우
                    W[w] = dist + weight
                    heapq.heappush(heap, (W[w], w)) # push


V, E = map(int, input().split())
K = int(input())
adj_l = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj_l[u].append((v, w))     # 방향 그래프

W = [987654321] * (V+1)
dijkstra(K)

for i in range(1, V+1):
    if W[i] == 987654321: print('INF')
    else: print(W[i])