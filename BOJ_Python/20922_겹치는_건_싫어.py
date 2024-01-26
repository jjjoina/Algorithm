import sys; input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

dic = {}
start_idx = -1
dp = [0] * N

for i in range(N):
    if lst[i] in dic:
        dic[lst[i]].append(i)
    else:
        dic[lst[i]] = [i]

    if len(dic[lst[i]]) > K:
        start_idx = dic[lst[i]].pop(0)

    dp[i] = i - start_idx

print(max(dp))