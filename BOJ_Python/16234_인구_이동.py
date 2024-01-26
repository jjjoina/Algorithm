import sys; input = sys.stdin.readline
from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = len(p_list)     # 방문 체크
    p.append(arr[i][j])
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and L <= abs(arr[ni][nj] - arr[i][j]) <= R:
                q.append((ni, nj))
                visited[ni][nj] = len(p_list)
                p.append(arr[ni][nj])


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:
    visited = [[0] * N for _ in range(N)]
    p_list = [0]    # p_list[i] : i번 연합의 평균 인구수
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                p = []  # 이 연합의 인구 리스트
                bfs(i, j)
                p_list.append(sum(p) // len(p))
    
    # 모든 나라가 각각 연합이면 while문 종료
    if len(p_list) == N*N+1: break

    # 인구 이동 반영
    for i in range(N):
        for j in range(N):
            arr[i][j] = p_list[visited[i][j]]
    
    ans += 1    # 하루 경과

print(ans)