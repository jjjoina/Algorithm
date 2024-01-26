# 풀이 2. [PyPy 192ms] DP
N = int(input())
dp = [i for i in range(N+1)]

for i in range(4, N+1):
    for j in range(1, int(i**0.5)+1):
        if dp[i] > dp[i - j*j] + 1:
            dp[i] = dp[i - j*j] + 1

print(dp[N])



# # 풀이 1. [PyPy 416ms] DP?
# N = int(input())

# lst = [i*i for i in range(1, int(N**0.5)+1)]
# cnt = 0
# ans = [0] * (N+1)

# for n in lst:
#     ans[n] = 1
#     cnt += 1

# rnd = 2
# A = lst[:]
# while cnt < N:
#     tmp = set()
#     for n1 in A:
#         for n2 in lst:
#             n = n1 + n2
#             if n <= N and ans[n] == 0:
#                 ans[n] = rnd
#                 tmp.add(n)
#                 cnt += 1
#     A = list(tmp)
#     rnd += 1

# print(ans[N])