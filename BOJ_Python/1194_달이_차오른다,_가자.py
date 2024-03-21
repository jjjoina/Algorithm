import sys; input = sys.stdin.readline
from collections import deque

KEYS = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
DOORS = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}

def find_start_point():
    for r in range(N):
        for c in range(M):
            if arr[r][c] == '0':
                return r, c


def bfs():
    q = deque()
    visited = [[[0] * 64 for _ in range(M)] for _ in range(N)]
    q.append((sr, sc, 0))
    visited[sr][sc][0] = 1

    while q:
        r, c, k = q.popleft()

        if arr[r][c] == '1':    # 출구인 경우
            return visited[r][c][k] - 1

        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != '#' and visited[nr][nc][k] == 0:
                # 문인 경우 매칭되는 열쇠가 없으면 continue
                if arr[nr][nc] in DOORS and (k >> DOORS[arr[nr][nc]]) % 2 == 0:
                    continue
                
                if arr[nr][nc] in KEYS:     # 열쇠 찾은 경우
                    nk = k | (1 << KEYS[arr[nr][nc]])
                    q.append((nr, nc, nk))
                    visited[nr][nc][nk] = visited[r][c][k] + 1
                else:
                    q.append((nr, nc, k))
                    visited[nr][nc][k] = visited[r][c][k] + 1

    return -1


N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

# for row in arr: print(arr)

sr, sc = find_start_point()

print(bfs())