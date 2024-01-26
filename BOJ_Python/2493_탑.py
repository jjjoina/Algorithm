# 풀이 2. [640ms] 앞에서 뒤로
import sys; input = sys.stdin.readline

N = int(input())
lst = [0] + list(map(int, input().split()))

stack = []
ans = [0] * (N+1)
for i in range(1, N+1):
    while stack:
        if stack[-1][0] < lst[i]:
            stack.pop()
        else:
            ans[i] = stack[-1][1]
            break
    stack.append((lst[i], i))

print(*ans[1:])


# # 풀이 1. [624ms] 뒤에서 앞으로
# import sys; input = sys.stdin.readline

# N = int(input())
# lst = [0] + list(map(int, input().split()))

# stack = []
# ans = [0] * (N+1)
# for i in range(N, 0, -1):
#     while stack and lst[i] > stack[-1][0]:
#         h, n = stack.pop()
#         ans[n] = i
#     stack.append((lst[i], i))

# print(*ans[1:])