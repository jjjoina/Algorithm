import sys; input = sys.stdin.readline
import heapq

INF = 300_000_000

def dijkstra(start):
    pq = [[0, start]]
    weights = [INF] * (N + 1)
    weights[start] = 0

    while pq:
        w, v = heapq.heappop(pq)

        if weights[v] < w:
            continue

        for nv, dw in adj_l[v]:
            nw = w + dw
            if weights[nv] > nw:
                heapq.heappush(pq, [nw, nv])
                weights[nv] = nw

    return weights


N, E = map(int, input().split())
adj_l = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adj_l[a].append([b, c])
    adj_l[b].append([a, c])
v1, v2 = map(int, input().split())

weights = dijkstra(v1)
v1_to_start = weights[1]
v1_to_v2 = weights[v2]
v1_to_end = weights[N]

weights = dijkstra(v2)
v2_to_start = weights[1]
v2_to_v1 = weights[v1]
v2_to_end = weights[N]

ans = INF

if v1_to_start != INF and v1_to_v2 != INF and v2_to_end != INF:
    ans = min(ans, v1_to_start + v1_to_v2 + v2_to_end)

if v2_to_start != INF and v1_to_v2 != INF and v1_to_end != INF:
    ans = min(ans, v2_to_start + v1_to_v2 + v1_to_end)

if ans == INF:
    ans = -1

print(ans)