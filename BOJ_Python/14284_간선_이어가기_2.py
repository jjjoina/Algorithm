import sys; input = sys.stdin.readline
import heapq

INF = 100000 * 100

def dijkstra():
    pq = [[0, s]]
    weights = [INF] * (n+1)
    weights[s] = 0
    
    while pq:
        w, v = heapq.heappop(pq)
        
        if w > weights[v]:
            continue
        
        # 최적화
        if v == t:
            return weights[t]
        
        for nv, dw in adj_l[v]:
            nw = w + dw
            if nw < weights[nv]:
                heapq.heappush(pq, [nw, nv])
                weights[nv] = nw


n, m = map(int, input().split())
adj_l = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj_l[a].append([b, c])
    adj_l[b].append([a, c])
s, t = map(int, input().split())

print(dijkstra())