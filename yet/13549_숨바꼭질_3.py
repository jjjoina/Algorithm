from collections import deque

N, K = map(int, input().split())
visited = [-1] * 100001
q = deque()
q.append(N)

# 시간 기록 (방문 체크)
t = N
while t <= 100000:
    q.append(t)
    visited[t] = 0 
    t *= 2

# BFS
while q:
    i = q.popleft()
    for ni in [i-1, i+1]:
        if 0 < ni <= 100000 and visited[ni] == -1:
            t = ni
            while t <= 100000:
                q.append(t)
                visited[t] = visited[i] + 1
                t *= 2

if K == 0:
    print(N)
else:    
    print(visited[K])