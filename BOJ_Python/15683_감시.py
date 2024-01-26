'''
N*M 사무실
CCTV K개
CCTV는 5종류
1: 1방
2: 2방 (180도)
3: 2방 (90도)
4: 3방
5: 4방
6: 벽
해당 방향의 벽 전까지 감시 가능
사각지대 : CCTV가 감시 불가능한 구역
CCTV 90도 회전 가능
CCTV는 CCTV를 통과할 수 있다.
최대한 많이 감시해보자!
'''

import sys; input = sys.stdin.readline

def dfs(i, dirs):
    '''
    i번째 CCTV의 방향 설정
    '''

    if i == K:
        film(dirs)  # 계산
        return

    for d_lst in dirs_by_case[CCTVs[i][2]]:
        dirs.append(d_lst)
        dfs(i+1, dirs)
        dirs.pop()
    

def film(dirs):
    global ans

    board = [[0] * M for _ in range(N)]
    # 각 칸은 arr에서 0이면서 CCTV가 감시하면 1로 마킹된다.

    for cctv in range(K):  # 각 CCTV마다
        for d in dirs[cctv]:   # 각 방향마다
            i, j = CCTVs[cctv][0], CCTVs[cctv][1]
            di, dj = dir4[d]
            while True:
                if i < 0 or i >= N or j < 0 or j >= M:    # 벗어난 경우
                    break
                if arr[i][j] == 6:  # 벽인 경우
                    break

                board[i][j] = 1

                i += di
                j += dj

    rst = 0     # 사각 지대의 개수
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and board[i][j] == 0: # CCTV나 벽이 없음 and 감시 못함 -> count
                rst += 1

    if ans > rst:
        ans = rst


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dir4 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# dirs_by_case[i] : i번 cctv가 감시할 수 있는 방향의 경우들의 리스트
dirs_by_case = [
        [],
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3] ,[3, 0]],
        [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
        [[0, 1, 2, 3]]
    ]

# CCTV 탐색
CCTVs = []
K = 0
for i in range(N):
    for j in range(M):
        if 1 <= arr[i][j] <= 5:
            CCTVs.append([i, j, arr[i][j]]) # arr[i][j] : cctv의 번호
            K += 1

# CCTV 방향 설정 (dfs)
ans = N * M
dfs(0, [])
print(ans)