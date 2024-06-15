import sys; input = sys.stdin.readline
import heapq

def dijkstra():
    pq = [[0, 0, 0]]
    weights = [[987654321] * n for _ in range(n)]
    weights[0][0] = 0
    
    while pq:
        w, r, c = heapq.heappop(pq)
        for dc, dr in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < n:
                nw = w if arr[nr][nc] else w+1
                if weights[nr][nc] > nw:
                    heapq.heappush(pq, [nw, nr, nc])
                    weights[nr][nc] = nw
    
    return weights[n-1][n-1]


n = int(input())
arr = [list(map(int, input().strip()))  for _ in range(n)]

print(dijkstra())