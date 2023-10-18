import sys; input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 0 : 청소되지 않은 빈 칸
# 9 : 청소된 빈 칸
# 1 : 벽

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ans = 0
while True:
    # 현재 칸이 아직 청소되지 않은 경우
    if arr[r][c] == 0:
        # 현재 칸을 청소한다.
        arr[r][c] = 9
        ans += 1
    
    # 주변 청소 상태 구하기
    not_clean = 0
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if arr[nr][nc] == 0:    # 벽으로 갇혀있어서 인덱스 체크는 필요 없다.
            not_clean += 1

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if not_clean == 0:
        # 후진했을 때의 좌표
        br, bc = r-dirs[d][0], c-dirs[d][1]
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면
        if arr[br][bc] != 1:
            # 후진하고 1번으로 돌아간다.
            r, c = br, bc
            continue
        # 후진할 수 없다면
        else:
            # 작동을 멈춘다.
            break

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    else:
        # 반시계 방향으로 90도 회전한다.
        d = (d - 1) % 4
        # 앞쪽 칸의 좌표
        fr, fc = r+dirs[d][0], c+dirs[d][1]
        # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우
        if arr[fr][fc] == 0:
            # 한 칸 전진한다.
            r, c = fr, fc

print(ans)