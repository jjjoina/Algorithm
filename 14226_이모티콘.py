import sys; input = sys.stdin.readline
from collections import deque

S = int(input())

visited = [[-1] * 1001 for _ in range(1001)]
q = deque([(1, 0)])
visited[1][0] = 0
while q:
    d, c = q.popleft()
    if d == S:
        print(visited[d][c])
        break

    # 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
    if visited[d][d] == -1:
        q.append((d, d))
        visited[d][d] = visited[d][c] + 1

    # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
    if c > 0 and d+c <= 1000 and visited[d+c][c] == -1:
        q.append((d+c, c))
        visited[d+c][c] = visited[d][c] + 1

    # 3. 화면에 있는 이모티콘 중 하나를 삭제
    if d > 0 and visited[d-1][c] == -1:
        q.append((d-1, c))
        visited[d-1][c] = visited[d][c] + 1