import sys; input = sys.stdin.readline
from collections import deque

dir4 = [[0, 1], [1, 0], [0, -1], [-1, 0]]

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

round = 0
q = deque()
q.append([-1, -1])
tmp = []

for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            tmp.append([i, j])

tmp.sort(key=lambda x: arr[x[0]][x[1]])
q.extend(tmp)

while q:
    i, j = q.popleft()

    if i == -1 and j == -1:     # round라운드 종료
        if round == S:
            break
        q.append([-1, -1])
        round += 1
        continue

    for di, dj in dir4:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            q.append([ni, nj])
            arr[ni][nj] = arr[i][j]

print(arr[X - 1][Y - 1])