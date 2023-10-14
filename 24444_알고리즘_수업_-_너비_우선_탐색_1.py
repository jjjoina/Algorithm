import sys; input = sys.stdin.readline
from collections import deque

def bfs(start):
    visited = [0] * (N+1)
    q = deque()
    q.append(start)
    visited[start] = 1
    cnt = 1
    while q:
        v = q.popleft()
        rst[v] = cnt
        cnt += 1
        adj_l[v].sort()
        for w in adj_l[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = 1


N, M, R = map(int, input().split())
adj_l = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj_l[u].append(v)
    adj_l[v].append(u)

rst = [0] * (N+1)
bfs(R)

for i in range(1, N+1):
    print(rst[i])