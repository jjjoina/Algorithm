import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
prev = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    prev[B].append(A)
X = int(input())

q = deque()
visited = [False] * (N+1)
q.append(X)
visited[X] = True
ans = 0
while q:
    v = q.popleft()
    for w in prev[v]:
        if not visited[w]:
            q.append(w)
            visited[w] = True
            ans += 1

print(ans)