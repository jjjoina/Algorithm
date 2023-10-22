import sys; input = sys.stdin.readline
from collections import deque

def bfs(start):
    global ans

    q = deque([start])
    visited[start] = 1
    while q:
        v = q.popleft()
        for w in adj_l[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = -visited[v]
            
            elif visited[w] == visited[v]:
                ans = 'NO'


def solve():
    checked = 1
    while checked <= V and ans == 'YES':    # 1~V번 정점 체크
        if visited[checked] == 0:           # 체크하지 않은 정점이면
            bfs(checked)                    # 체크
        checked += 1


for _ in range(int(input())):
    V, E = map(int, input().split())
    adj_l = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj_l[u].append(v)
        adj_l[v].append(u)
    
    visited = [0] * (V+1)
    ans = 'YES'
    solve()
    print(ans)