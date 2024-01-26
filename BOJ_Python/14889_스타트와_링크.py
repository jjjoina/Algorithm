import sys; input = sys.stdin.readline

def comb(i, start):
    global ans

    if i == N//2:
        points = [0, 0]
        for k in range(N-1):
            for l in range(k+1, N):
                if used[k] == used[l]:
                    points[used[k]] += arr[k][l] + arr[l][k]

        ans = min(ans, abs(points[0] - points[1]))
        return

    for j in range(start, N//2 + i):
        if used[j] == 0:
            c.append(j)
            used[j] = 1
            comb(i+1, j+1)
            c.pop()
            used[j] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

used = [0] * N
c = []
ans = 987654321

comb(0, 0)

print(ans)