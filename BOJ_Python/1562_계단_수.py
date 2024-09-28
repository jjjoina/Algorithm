MOD = 1_000_000_000

N = int(input())

dp = [[0] * 10 for _ in range(1 << 10)]

for last in range(1, 10):
    dp[1 << last][last] = 1

for _ in range(N - 1):
    temp = [[0] * 10 for _ in range(1 << 10)]

    for bit in range(1 << 10):
        for last in range(10):
            if last != 0:
                temp[bit | (1 << last - 1)][last - 1] = (temp[bit | (1 << last - 1)][last - 1] + dp[bit][last]) % MOD
            if last != 9:
                temp[bit | (1 << last + 1)][last + 1] = (temp[bit | (1 << last + 1)][last + 1] + dp[bit][last]) % MOD

    dp = temp

print(sum(dp[(1 << 10) - 1]) % MOD)