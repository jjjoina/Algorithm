def dc(N, r, c):
    if N == 3:
        ans[r][c] = '*'
        ans[r+1][c-1] = ans[r+1][c+1] = '*'
        ans[r+2][c-2:c+3] = ['*'] * 5
        return

    N //= 2
    dc(N, r, c)
    dc(N, r+N, c-N)
    dc(N, r+N, c+N)


N = int(input())

ans = [[' '] * (2*N-1) for _ in range(N)]

dc(N, 0, N-1)

for row in ans:
    print(''.join(row))