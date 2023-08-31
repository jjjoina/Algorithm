coins = [25, 10, 5, 1]

T = int(input())
for t in range(1, T+1):
    ans = [0] * 4
    C = int(input())
    for i in range(4):
        ans[i] += C // coins[i]
        C %= coins[i]
    print(*ans)