import sys; input = sys.stdin.readline
from collections import deque

dir2 = [[0, 1], [1, 0]]
dir4 = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def calculate_indegree():
    indegree = [[0] * N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            for di, dj in dir2:
                ni = i + di
                nj = j + dj

                if ni < M and nj < N:
                    if arr[i][j] > arr[ni][nj]:
                        indegree[ni][nj] += 1
                    elif arr[i][j] < arr[ni][nj]:
                        indegree[i][j] += 1

    return indegree


def topological_sort():
    q = deque()
    count = [[0] * N for _ in range(M)]
    count[0][0] = 1

    for i in range(M):
        for j in range(N):
            if indegree[i][j] == 0:
                q.append([i, j])

    while q:
        i, j = q.popleft()

        if i == M - 1 and j == N - 1:
            break

        for di, dj in dir4:
            ni = i + di
            nj = j + dj

            if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] < arr[i][j]:
                count[ni][nj] += count[i][j]

                indegree[ni][nj] -= 1

                if indegree[ni][nj] == 0:
                    q.append([ni, nj])

    return count[M - 1][N - 1]


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

indegree = calculate_indegree()

print(topological_sort())