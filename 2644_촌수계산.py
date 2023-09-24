import sys; input = sys.stdin.readline
from collections import deque

def bfs(a, b):
    q = deque([(a)])
    visited[a] = 0
    while q:
        v = q.popleft()
        for w in adj_l[v]:
            if visited[w] == -1:
                q.append(w)
                visited[w] = visited[v] + 1
                if w == b: return


n = int(input())    # 1 ~ n
a, b = map(int, input().split())
m = int(input())
adj_l = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    # x와 y는 인접함
    adj_l[x].append(y)
    adj_l[y].append(x)

visited = [-1] * (n+1)
bfs(a, b)
print(visited[b])