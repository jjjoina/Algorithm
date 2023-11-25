# 풀이 2. DP
N = int(input())

dp = [1] * 10
for _ in range(N):
    for i in range(1, 10):
        dp[i] += dp[i-1]

print(dp[-1] % 10007)



# # 풀이 1. [40ms] 중복조합
# N = int(input())

# ans = 1
# for i in range(1, 10):
#     ans *= N+i
# for i in range(1, 10):
#     ans //= i

# print(ans % 10007)