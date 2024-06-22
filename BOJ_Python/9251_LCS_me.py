import sys; input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

len_s1 = len(s1)
len_s2 = len(s2)

common = [[0] * len_s2 for _ in range(len_s1)]
for i in range(len_s1):
    for j in range(len_s2):
        if s1[i] == s2[j]:
            common[i][j] = 1
            
dp = [[0] * len_s2 for _ in range(len_s1)]
for i in range(len_s1):     # 0열 초기화
    dp[i][0] = common[i][0]
for j in range(len_s2):     # 0행 초기화
    dp[0][j] = common[0][j]

for i in range(1, len_s1):
    for j in range(1, len_s2):
        dp[i][j] = max(
            dp[i-1][j-1],
            dp[i-1][j] - common[i-1][j],
            dp[i][j-1] - common[i][j-1]
            ) + common[i][j]
    
print(max(map(max, dp)))