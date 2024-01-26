import sys; input = sys.stdin.readline
from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        for w in adj_l[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = 1


N, M = map(int, input().split())
adj_l = [[] for _ in range(N+1)]  # 1 ~ N번 정점들 간의 인접 리스트

for _ in range(M):
    u, v = map(int, input().split())
    adj_l[u].append(v)
    adj_l[v].append(u)

visited = [0] * (N+1)
ans = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        ans += 1
print(ans)