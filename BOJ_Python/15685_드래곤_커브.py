import sys; input = sys.stdin.readline

dragon = [[] for _ in range(11)]
dragon[1] = [1]
for i in range(2, 11):
    tmp = dragon[i-1][::-1]
    for j in range(len(tmp)):
        tmp[j] *= -1
    dragon[i] = dragon[i-1] + [1] + tmp

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

N = int(input())
arr = [[0] * 101 for _ in range(101)]
for i in range(1, N+1):
    c, r, d, g = map(int, input().split())
    arr[r][c] = i
    r += dr[d]
    c += dc[d]
    arr[r][c] = i

    for dd in dragon[g]:
        d = (d + dd) % 4
        r += dr[d]
        c += dc[d]
        arr[r][c] = i

# for row in arr: print(*row)

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] > 0 and arr[i][j+1] > 0 and arr[i+1][j] > 0 and arr[i+1][j+1] > 0:
            ans += 1

print(ans)