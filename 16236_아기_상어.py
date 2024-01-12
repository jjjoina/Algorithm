import sys; input = sys.stdin.readline
from collections import deque

def find_start_point():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return i, j
            
            
def look_up(r, c):
    global i, j, shark, cnt

    visited = [[-1] * N for _ in range(N)]
    q = deque()
    visited[r][c] = 0
    q.append([r, c])
    
    while q:
        r, c = q.popleft()  # visited의 오름차순으로 꺼내게 된다.

        if 0 < arr[r][c] < shark:
            dist = visited[r][c]
            # 큐에 있는 것 : 빈칸, 작은 물고기, 같은 물고기
            # 같은 거리의 칸들 중 먹을 물고기(r, c) 특정 짓기
            while q:
                x, y = q.popleft()
                
                if visited[x][y] > dist:    # 가장 가까운 물고기가 아님
                    break

                if 0 < arr[x][y] < shark:   # 작은 물고기인 경우
                    if r > x:
                        r, c = x, y         # 위에 있는 물고기 선택
                    elif r == x:
                        if c > y:
                            c = y           # 왼쪽에 있는 물고기 선택

            arr[i][j] = 0   # 상어 떠남
            i, j = r, c     # 먹으러 이동
            arr[i][j] = 0   # 먹음

            cnt += 1
            if cnt == shark:
                shark += 1
                cnt = 0
            
            return dist
            
        for dr, dc in [[-1, 0], [0, -1], [0, 1], [1, 0]]:   # 상좌우하
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                # 방문한 적 없고 지나갈 수 있으면 지나감
                if arr[nr][nc] <= shark:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append([nr, nc])

    # 물고기가 없는 경우
    return False


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

i, j = find_start_point()   # 상어 좌표
shark = 2
cnt = 0
ans = 0

while True:
    rst = look_up(i, j) # 물고기 탐색 (bfs) (크기에 따라)
    if rst == False:    # 없는 경우 종료
        break
    ans += rst

print(ans)