import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
move = [i for i in range(101)]
# i번째 칸에 도착하면 move[i]로 이동
for _ in range(N + M):
    f, t = map(int, input().split())
    move[f] = t

visited = [0] * 101
q = deque([1])
while q:
    v = q.popleft()
    for w in range(v+1, v+7):
        if w <= 100 and visited[w] == 0:
            if w == move[w]:
                q.append(w)
                visited[w] = visited[v] + 1
                if w == 100:
                    break
            else:
                if visited[move[w]] == 0:
                    q.append(move[w])
                    visited[move[w]] = visited[w] = visited[v] + 1
                else:
                    visited[w] = visited[v] + 1
    
print(visited[100])