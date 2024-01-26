from collections import deque

visited = [-1] * 100001
N, K = map(int, input().split())

# BFS
q = deque()
q.append(N)
visited[N] = 0
while q:
    t = q.popleft()
    if t == K:
        print(visited[t])
        break
    
    for nt in [t-1, t+1, 2*t]:
        if 0 <= nt < 100001 and visited[nt] == -1:
            q.append(nt)
            visited[nt] = visited[t] + 1