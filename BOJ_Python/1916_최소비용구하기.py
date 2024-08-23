import sys; input = sys.stdin.readline
import heapq

MAX = 100_000_000

N = int(input())
M = int(input())
adj_l = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    adj_l[s].append([e, w])
s, e = map(int, input().split())

pq = []
weights = [MAX] * (N + 1)

pq.append([0, s])
weights[s] = 0

while pq:
    w, v = heapq.heappop(pq)

    if weights[v] != w:
        continue

    if v == e:
        print(w)
        break

    for nv, dw in adj_l[v]:
        nw = w + dw
        if weights[nv] > nw:
            heapq.heappush(pq, [nw, nv])
            weights[nv] = nw