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
        r, c = q.popleft()

        if 0 < arr[r][c] < shark:
            
            # print('---------------------------')
            # print(f'shark={shark}, cnt={cnt} (before eat)')
            # print()
            # print(q)
            
            # 큐에 있는 것 : 빈칸, 작은 물고기, 같은 물고기
            # 같은 거리의 칸들 중 먹을 물고기 특정 짓기
            for x, y in q:
                if visited[x][y] > visited[r][c]:
                    break

                if 0 < arr[x][y] < shark:
                    if r > x:
                        r, c = x, y
                    elif r == x:
                        if c > y:
                            c = y

            arr[i][j] = 0
            i, j = r, c
            arr[i][j] = 9

            cnt += 1
            if cnt == shark:
                shark += 1
                cnt = 0

            # for row in arr: print(*row)
            # print()
            # print(f'ate ({i}, {j})')
            # print(f'ans += {visited[r][c]}')
            # print(f'shark={shark}, cnt={cnt} (after eat)')
            
            return visited[r][c]
            
        for dr, dc in [[-1, 0], [0, -1], [0, 1], [1, 0]]:   # 상좌우하
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                if arr[nr][nc] <= shark:
                    # 이어서 탐색
                    visited[nr][nc] = visited[r][c] + 1
                    q.append([nr, nc])
                    # print(nr, nc, visited[nr][nc])

    # 물고기가 없는 경우
    return 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

i, j = find_start_point()
shark = 2
cnt = 0
ans = 0

while True:
    rst = look_up(i, j) # 물고기 탐색 (bfs) (크기에 따라)
    if rst == 0:    # 없는 경우 종료
        break
    ans += rst

print(ans)