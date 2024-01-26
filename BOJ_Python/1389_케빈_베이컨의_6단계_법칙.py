import sys; input = sys.stdin.readline
from collections import deque

def KB(start):
    visited = [-1] * (N+1)
    q = deque()
    q.append(start)
    visited[start] = 0
    while q:
        v = q.popleft()
        for w in range(1, N+1):
            if adj_m[v][w] == 1 and visited[w] == -1:
                q.append(w)
                visited[w] = visited[v] + 1

    return sum(visited[1:])


N, M = map(int, input().split())
adj_m = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    adj_m[A][B] = 1
    adj_m[B][A] = 1

min_KBN = 987654321
for i in range(1, N+1):
    KBN = KB(i)
    if min_KBN > KBN:
        min_KBN = KBN
        ans = i

print(ans)