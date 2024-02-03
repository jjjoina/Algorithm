import sys; input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    visited = [-1] * N
    q.append(a)
    visited[a] = 0

    while q:
        v = q.popleft()
        if v == b:
            return visited[b]

        for w in range(v, N, lst[v]):
            if visited[w] == -1:
                q.append(w)
                visited[w] = visited[v] + 1

        for w in range(v, -1, -lst[v]):
            if visited[w] == -1:
                q.append(w)
                visited[w] = visited[v] + 1

    return -1

            
N = int(input())
lst = list(map(int, input().split()))
a, b = map(int, input().split())
a -= 1
b -= 1

print(bfs())