H, Y = map(int, input().split())

dp = [H] + [0] * Y

for y in range(1, Y+1):
    a = dp[y-1] * 1.05 if y >= 1 else 0
    b = dp[y-3] * 1.2 if y >= 3 else 0
    c = dp[y-5] * 1.35 if y >= 5 else 0
    
    dp[y] = int(max(a, b, c))

print(dp[y])