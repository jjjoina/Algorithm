import sys; input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    q = deque()
    visited = [False] * 10000
    q.append([A, ''])
    visited[A] = True

    while q:
        n, c = q.popleft()

        if n == B:
            print(c)
            break

        d = n * 2 % 10000
        if not visited[d]:
            q.append([d, c+'D'])
            visited[d] = True

        s = (n - 1) % 10000
        if not visited[s]:
            q.append([s, c+'S'])
            visited[s] = True

        l = n * 10 % 10000 + n // 1000
        if not visited[l]:
            q.append([l, c+'L'])
            visited[l] = True

        r = n % 10 * 1000 + n // 10
        if not visited[r]:
            q.append([r, c+'R'])
            visited[r] = True