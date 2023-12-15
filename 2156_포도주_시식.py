import sys; input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

dp = [0, lst[0], 0]

for i in range(1, N):    
    dp = [max(dp), dp[0]+lst[i], dp[1]+lst[i]]

print(max(dp))