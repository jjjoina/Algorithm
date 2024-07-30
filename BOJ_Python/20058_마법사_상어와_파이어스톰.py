import sys; input = sys.stdin.readline
from collections import deque

def rotate(si, sj, s):
    q = deque()

    for i in range(si, si + s):
        for j in range(sj, sj + s):
            q.append(A[i][j])

    for j in range(sj + s - 1, sj - 1, -1):
        for i in range(si, si + s):
            A[i][j] = q.popleft()


def melt():
    tmp = []

    for i in range(size):
        for j in range(size):
            if A[i][j] == 0:
                continue

            cnt = 0

            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < size and 0 <= nj < size and A[ni][nj] > 0:
                    cnt += 1

            if cnt < 3:
                tmp.append([i, j])

    while tmp:
        i, j = tmp.pop()
        A[i][j] -= 1


def bfs(si, sj, visited):
    q = deque()
    q.append([si, sj])
    visited[si][sj] = True
    cnt = 0

    while q:
        i, j = q.popleft()

        cnt += 1

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < size and 0 <= nj < size and not visited[ni][nj] and A[ni][nj] > 0:
                q.append([ni, nj])
                visited[ni][nj] = True

    return cnt


def print_answer():
    ans_sum = 0
    ans_max = 0
    visited = [[False] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if A[i][j] == 0:
                continue

            ans_sum += A[i][j]

            if not visited[i][j]:
                cnt = bfs(i, j, visited)
                if ans_max < cnt:
                    ans_max = cnt

    print(ans_sum)
    print(ans_max)


N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2 ** N)]
L = list(map(int, input().split()))

size = 2 ** N

for l in L:
    s = 2 ** l

    for i in range(0, size, s):
        for j in range(0, size, s):
            rotate(i, j, s)

    melt()

print_answer()