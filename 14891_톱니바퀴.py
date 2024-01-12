import sys; input = sys.stdin.readline

gears = [list(map(int, input().strip())) for _ in range(4)]
K = int(input())

for _ in range(K):
    n, d = map(int, input().split())
    n -= 1

    d_lst = [0] * 4
    d_lst[n] = d

    for i in range(n-1, -1, -1):
        if gears[i][2] != gears[i+1][6]:
            d_lst[i] = -d_lst[i+1]
        else:
            break

    for i in range(n+1, 4):
        if gears[i][6] != gears[i-1][2]:
            d_lst[i] = -d_lst[i-1]
        else:
            break

    for i in range(4):
        if d_lst[i] == -1:
            gears[i] = gears[i][1:] + gears[i][:1]
        elif d_lst[i] == 1:
            gears[i] = gears[i][7:] + gears[i][:7]

ans = 0
for i in range(4):
    if gears[i][0] == 1:
        ans += 2 ** i
print(ans)