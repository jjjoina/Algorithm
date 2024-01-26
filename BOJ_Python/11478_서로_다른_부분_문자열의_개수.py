# 풀이 2. [정답] [248ms] 입력이 1000밖에 되지 않음을 이용 (2중 for문)

import sys; input = sys.stdin.readline

S = input().strip()
N = len(S)
ans = 0
for i in range(1, N+1):
    p = set()
    for j in range(N-i+1):
        p.add(S[j:j+i])
    ans += len(p)
print(ans)



# # 풀이 1. [정답] [1392ms] 재귀

# import sys; input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def solve(s):
#     n = len(s)
#     if n == 1: return

#     if s[:n-1] not in my_set:
#         my_set.add(s[:n-1])
#         solve(s[:n-1])
#     if s[1:] not in my_set:
#         my_set.add(s[1:])
#         solve(s[1:])


# S = input().strip()
# my_set = {S}
# solve(S)
# print(len(my_set))