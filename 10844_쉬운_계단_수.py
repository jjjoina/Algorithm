N = int(input())

dp = [0] + [1] * 9  # dp[i] : 끝자리가 i인 계단 수의 개수

for _ in range(N-1):
    dp = [
        dp[1],
        dp[0] + dp[2],
        dp[1] + dp[3],
        dp[2] + dp[4],
        dp[3] + dp[5],
        dp[4] + dp[6],
        dp[5] + dp[7],
        dp[6] + dp[8],
        dp[7] + dp[9],
        dp[8]
    ]

    for i in range(10):
        dp[i] %= 1_000_000_000

print(sum(dp) % 1_000_000_000)