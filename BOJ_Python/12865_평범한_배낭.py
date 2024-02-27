# # 풀이 3. 풀이 2 최적화
# import sys; input = sys.stdin.readline

# N, K = map(int, input().split())

# dp = [0] * (K+1)

# for _ in range(N):
#     W, V = map(int, input().split())
#     for kw in range(K, W-1, -1):    # kw : knapsack weight
#         dp[kw] = max(dp[kw], V + dp[kw-W])

# print(dp[K])



# 풀이 2. 0-1 배낭 문제
import sys; input = sys.stdin.readline

N, K = map(int, input().split())

# dp 계산의 편의를 위해 index 1부터 입력
things = [[]] + [list(map(int, input().split())) for _ in range(N)]

# dp[i][w] := 최대 하중이 w인 배낭에 물건 1,2,...,i를 담을 때 총 가치의 최대값
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for w in range(K+1):
        if things[i][0] > w:    # 물건을 배낭에 넣지 못 하는 경우
            # 해당 물건을 제외하고 생각한 경우의 최대값
            dp[i][w] = dp[i-1][w]

        else:                   # 물건을 배낭에 넣을 수 있는 경우
            # 두 가지 경우 중 큰 값
            # (1) 물건 i를 넣지 않는 경우
            #     -> 물건 i를 제외하고 생각한 경우의 최대값
            # (2) 물건 i를 넣는 경우
            #     -> 물건 i의 가치 + 물건 i를 제외, 배낭의 최대 하중이 (w-물건 i의 무게)인 경우의 최대값
            dp[i][w] = max(dp[i-1][w], things[i][1] + dp[i-1][w-things[i][0]])

print(dp[N][K])     # 정답 = 최대 하중이 K인 배낭에 물건 1,2,...,N을 담을 때 총 가치의 최대값



# # 풀이 1. 오답
# import sys; input = sys.stdin.readline

# N, K = map(int, input().split())
# things = [list(map(int, input().split())) for _ in range(N)]

# things.sort(key=lambda x:(x[1]/x[0]), reverse=True)
# # print(things)

# idx = 0
# sum_w = 0
# sum_v = 0
# bp = []
# ans = 0

# while True:
#     while idx < N:
#         if sum_w + things[idx][0] <= K:
#             bp.append(idx)
#             sum_w += things[idx][0]
#             sum_v += things[idx][1]
#         idx += 1

#     if ans < sum_v:
#         ans = sum_v
    
#     if sum_w == K:
#         break

#     # print(bp)
#     # print(ans, bp)

#     idx = bp.pop()
#     if idx == N-1 and not bp:
#         break
#     sum_w -= things[idx][0]
#     sum_v -= things[idx][1]
#     idx += 1

# print(ans)