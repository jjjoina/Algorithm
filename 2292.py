n = int(input())
ans = 1     # 현재 바퀴
max_v = 1   # 현재 바퀴의 최대 수
while True:
    if n <= max_v:
        break 
    max_v += ans * 6    # 1, 7, 29, 37, ...
    ans += 1
print(ans)

# def a(n):
#     return 3*n*(n-1) + 1

# n = int(input())
# ans = 1
# while True:
#     if a(ans) >= n:
#         break
#     ans += 1
# print(ans)

# 재귀 풀이 (런타임 에러)
# def a(n):
#     if n == 1:
#         return 1
#     else:
#         return a(n-1) + 6*(n-1)

# n = int(input())
# ans = 1
# while True:
#     if a(ans) >= n:
#         break
#     ans += 1
# print(ans)