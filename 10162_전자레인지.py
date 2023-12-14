T = int(input())

if T % 10 != 0:
    print(-1)
else:
    btn = [300, 60, 10]
    ans = [0, 0, 0]

    for i in range(3):
        ans[i] += T // btn[i]
        T %= btn[i]

    print(*ans)