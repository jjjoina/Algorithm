import sys; input = sys.stdin.readline
from collections import deque
from copy import deepcopy

def mark_outside_air():
    # 외부 공기를 cnt로 마킹
    q = deque([(0, 0)])
    cur[0][0] = cnt
    
    # BFS
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and cur[ni][nj] != 1 and cur[ni][nj] != cnt:
                q.append((ni, nj))
                cur[ni][nj] = cnt   # 마킹


def mark_cheese_to_melt():
    global cheese_exist

    for i in range(N):
        for j in range(M):
            if cur[i][j] == 1:
                cnt_dir = 0
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    ni, nj = i+di, j+dj
                    if cur[ni][nj] == cnt:
                        cnt_dir += 1
                if cnt_dir >= 2:
                    nxt[i][j] = 0
                else:
                    cheese_exist = True
                    

N, M = map(int, input().split())
cur = [list(map(int, input().split())) for _ in range(N)]

cnt = -1
while True:
    mark_outside_air()      # 외부 공기를 cnt로 표시
    nxt = deepcopy(cur)
    cheese_exist = False
    mark_cheese_to_melt()   # 녹을 치즈들을 nxt에 0으로 표시
                            # 동시에 치즈가 남아있는지도 체크
    if not cheese_exist: break
    cur = deepcopy(nxt)
    cnt -= 1

print(-cnt)