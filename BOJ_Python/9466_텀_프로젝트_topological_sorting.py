import sys; input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    nv = [0] + list(map(int, input().split()))

    indegree = [0] * (n + 1)
    for v in range(1, n + 1):
        indegree[nv[v]] += 1

    q = deque()
    ans = 0
    for v in range(1, n + 1):
        if indegree[v] == 0:
            q.append(v)
            ans += 1

    while q:
        v = q.popleft()
        indegree[nv[v]] -= 1
        if indegree[nv[v]] == 0:
            q.append(nv[v])
            ans += 1

    print(ans)