import sys; input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# 껍질 저장
skins = []

visited = [[0] * M for _ in range(N)]
n = 0
while True:
    i = j = n
    
    if visited[i][j] == 1:
        break

    skins.append([])
    for d in range(4):
        if d > 0:
            i += dir[d][0]
            j += dir[d][1]
        while True:
            if 0 <= i < N and 0 <= j < M and visited[i][j] == 0:
                skins[n].append(arr[i][j])
                visited[i][j] = 1
                i += dir[d][0]
                j += dir[d][1]
            else:
                i -= dir[d][0]
                j -= dir[d][1]
                break
    n += 1

# 껍질 회전
for i in range(len(skins)):
    l = len(skins[i])
    idx = l - R % l
    if idx > 0:
        skins[i] = skins[i][idx:] + skins[i][:idx]

# 껍질 원위치
visited = [[0] * M for _ in range(N)]
n = 0
while True:
    i = j = n
    
    if visited[i][j] == 1:
        break

    cnt = 0
    for d in range(4):
        if d > 0:
            i += dir[d][0]
            j += dir[d][1]
        while True:
            if 0 <= i < N and 0 <= j < M and visited[i][j] == 0:
                arr[i][j] = skins[n][cnt]
                cnt += 1
                visited[i][j] = 1
                i += dir[d][0]
                j += dir[d][1]
            else:
                i -= dir[d][0]
                j -= dir[d][1]
                break
    n += 1

for row in arr:
    print(*row)