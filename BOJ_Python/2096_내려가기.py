import sys; input = sys.stdin.readline

N = int(input())

max_dp = list(map(int, input().split()))
min_dp = max_dp[::]

for _ in range(N - 1):
    line = list(map(int, input().split()))

    max_dp = [
        max(max_dp[:2]) + line[0],
        max(max_dp) + line[1],
        max(max_dp[1:]) + line[2]
    ]

    min_dp = [
        min(min_dp[:2]) + line[0],
        min(min_dp) + line[1],
        min(min_dp[1:]) + line[2]
    ]

print(max(max_dp), min(min_dp))