def star(i, j, n):
    if n == 1:
        arr[i][j] = '*'
        return

    n //= 3

    for di in range(3):
        for dj in range(3):
            if di == 1 and dj == 1:
                continue
            
            ni = i + di * n
            nj = j + dj * n
            
            star(ni, nj, n)


N = int(input())

arr = [[' '] * N for _ in range(N)]

star(0, 0, N)

for row in arr:
    print(''.join(row))