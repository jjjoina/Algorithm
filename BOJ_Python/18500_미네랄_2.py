import sys; input = sys.stdin.readline
from collections import deque

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def throw(i):
    r = heights[i]
    c = 0 if i % 2 == 0 else C-1
    dc = 1 if i % 2 == 0 else -1

    while 0 <= c < C:
        if cave[r][c] == 'x':
            return r, c
        c += dc

    return r, -1


def is_levitated(r, c):
    q = deque()
    visited = [[False] * C for _ in range(R)]
    q.append([r, c])
    visited[r][c] = True

    while q:
        r, c = q.popleft()
        if r == R-1:
            return False
        
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and cave[nr][nc] == 'x' and not visited[nr][nc]:
                q.append([nr, nc])
                visited[nr][nc] = True

    return True


def fall(sr, sc):
    q = deque()
    is_cluster = [[False] * C for _ in range(R)]
    q.append([sr, sc])
    is_cluster[sr][sc] = True
    bottoms = []

    while q:
        r, c = q.popleft()
        if cave[r+1][c] == '.':
            bottoms.append([r, c])
        
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and cave[nr][nc] == 'x' and not is_cluster[nr][nc]:
                q.append([nr, nc])
                is_cluster[nr][nc] = True

    # 떨어지는 높이 도출
    fall_height = 100
    for r, c in bottoms:
        cnt = 1
        while r+cnt+1 < R and (cave[r+cnt+1][c] == '.' or is_cluster[r+cnt+1][c]):
            cnt += 1
        if fall_height > cnt:
            fall_height = cnt
    
    # 낙하
    for r in range(R-1, -1, -1):    # 가장 아래 행부터 낙하
        for c in range(C):
            if is_cluster[r][c]:
                cave[r][c] = '.'
                cave[r+fall_height][c] = 'x'


R, C = map(int, input().split())
cave = [list(input().strip()) for _ in range(R)]
N = int(input())
heights = list(map(lambda x: R-int(x), input().split()))

for i in range(N):
    r, c = throw(i)
    if c == -1:
        continue
    cave[r][c] = '.'
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if 0 <= nr < R and 0 <= nc < C and cave[nr][nc] == 'x' and is_levitated(nr, nc):
            fall(nr, nc)
            break

for row in cave:
    print(''.join(row))