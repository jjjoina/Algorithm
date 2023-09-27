def N_Queen(i):
    # i행에서 j열에 퀸 착수하는 함수
    global ans

    if i == N:
        ans += 1
        return
    
    for j in range(N):
        if not visited[i][j]:
            mark(i+1, j, 1)
            N_Queen(i+1)
            mark(i+1, j, -1)


def mark(i, j, v):
    d = 1
    while i < N:
        visited[i][j] += v                  # 하향
        if 0 <= j-d: visited[i][j-d] += v   # 좌하향
        if j+d < N: visited[i][j+d] += v    # 우하향
        i += 1
        d += 1


N = int(input())
ans = 0
visited = [[0] * N for _ in range(N)]
N_Queen(0)
print(ans)