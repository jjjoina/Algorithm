import sys; input = sys.stdin.readline

# (경우의 수, 그 중 3을 포함하지 않은 것의 수)
dp = [(0, 0), (1, 1), (2, 2), (3, 2)]
for i in range(4, 10001):
    all = dp[i-3][0] + dp[i-2][1] + 1
    no3 = dp[i-2][1] + 1
    dp.append((all, no3))

for _ in range(int(input())):
    print(dp[int(input())][0])