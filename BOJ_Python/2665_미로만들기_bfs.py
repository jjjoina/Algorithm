import sys; input = sys.stdin.readline
import heapq

def bfs():
    pq = [[0, 0, 0]]
    visited = [[-1] * n for _ in range(n)]
    visited[0][0] = 0
    
    while pq:
        cnt, r, c = heapq.heappop(pq)
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == -1:
                ncnt = cnt if arr[nr][nc] else cnt+1
                heapq.heappush(pq, [ncnt, nr, nc])
                visited[nr][nc] = ncnt
                
                if nr == n-1 and nc == n-1:
                    return visited[nr][nc]


n = int(input())
arr = [list(map(int, input().strip())) for _ in range(n)]

print(bfs())