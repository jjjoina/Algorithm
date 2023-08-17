# 풀이 2. memoization
# cnt_0, cnt_1도 피보나치 수열임을 발견!
def fibo(N):
    memo = [0, 1]
    for i in range(2, N+1):
        memo.append(memo[i-1] + memo[i-2])
    return memo[N-1], memo[N]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(*fibo(N))


# # 풀이 1. 시간 초과
# def fibo(N):
#     global cnt_0
#     global cnt_1

#     if N == 0:
#         cnt_0 += 1
#         return 0
    
#     elif N == 1:
#         cnt_1 += 1
#         return 1
    
#     else:
#         return fibo(N-2) + fibo(N-1)

# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     cnt_0 = cnt_1 = 0
#     fibo(N)
#     print(cnt_0, cnt_1)