import sys; input = sys.stdin.readline
from collections import deque

def rotate(x, d, k):
    if d == 1:
        k = M - k

    for i in range(x, N + 1, x):
        arr[i].rotate(k)


def bfs(si, sj, visited):
    q = deque()
    q.append([si, sj])
    visited[si][sj] = True
    result = False

    while q:
        i, j = q.popleft()

        for di, dj in dir4:
            ni = i + di
            nj = (j + dj) % M

            if 1 <= ni <= N and not visited[ni][nj] and arr[ni][nj] == arr[si][sj]:
                q.append([ni, nj])
                visited[ni][nj] = True
                arr[ni][nj] = 0
                result = True

    if result:
        arr[si][sj] = 0

    return result


def update():
    sum_ = 0
    count = 0

    for i in range(1, N + 1):
        for j in range(M):
            if arr[i][j] > 0:
                sum_ += arr[i][j]
                count += 1

    if count == 0:
        return

    average = sum_ / count

    for i in range(1, N + 1):
        for j in range(M):
            if arr[i][j] > average:
                arr[i][j] -= 1
            elif 0 < arr[i][j] < average:
                arr[i][j] += 1


def erase():
    visited = [[False] * M for _ in range(N + 1)]
    result = False

    for i in range(1, N + 1):
        for j in range(M):
            if arr[i][j] > 0 and not visited[i][j]:
                result |= bfs(i, j, visited)

    if not result:
        update()


N, M, T = map(int, input().split())
arr = [deque()] + [deque(map(int, input().split())) for _ in range(N)]

dir4 = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for _ in range(T):
    x, d, k = map(int, input().split())
    rotate(x, d, k)
    erase()

print(sum(map(sum, arr)))