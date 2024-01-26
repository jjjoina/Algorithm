import sys; input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
for i in range(1, N):
    max_length = 0
    for j in range(i):
        if A[j] < A[i] and max_length < dp[j]:
            max_length = dp[j]
    dp[i] = max_length + 1
    
print(max(dp))