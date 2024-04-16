# 풀이 2. [436ms] 누적합
zeros = [1] * 1_000_001
for i in range(1, 1_000_001):
    zeros[i] = zeros[i-1] + str(i).count('0')

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    if N == 0:
        print(zeros[M])
    else:
        print(zeros[M] - zeros[N-1])


# # 풀이 1. [4476ms] 브루트 포스

# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     ans = 0
#     for i in range(N, M+1):
#         s = str(i)
#         for c in s:
#             if c == '0':
#                 ans += 1
    
#     print(ans)