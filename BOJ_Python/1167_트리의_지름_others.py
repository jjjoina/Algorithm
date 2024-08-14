import sys; input = sys.stdin.readline
from collections import deque

def bfs(s):
    q = deque()
    visited = [-1] * (V + 1)
    q.append(s)
    visited[s] = 0

    while q:
        v = q.popleft()
        for w, l in adj_l[v]:
            if visited[w] == -1:
                q.append(w)
                visited[w] = visited[v] + l

    max_l = 0
    max_idx = 0

    for v in range(1, V + 1):
        if max_l < visited[v]:
            max_l = visited[v]
            max_idx = v

    return max_l, max_idx


V = int(input())

adj_l = [[] for _ in range(V + 1)]

for _ in range(V):
    v, *info = (map(int, input().split()))

    for i in range(0, len(info) - 1, 2):
        adj_l[v].append([info[i], info[i + 1]])

visited = [False] * (V + 1)

_, v = bfs(1)
ans, _ = bfs(v)

print(ans)