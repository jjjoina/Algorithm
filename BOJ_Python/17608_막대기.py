# 풀이 2. 스택
import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    h = int(sys.stdin.readline())
    # 스택이 비어있는 경우 or 스택에 원소가 있고 top 원소가 h보다 큰 경우
    if not stack or stack[-1] > h:
        stack.append(h)
    # 스택에 원소가 있고 h보다 작은 경우
    elif stack and stack[-1] < h:
        while True:
            # stack이 비게 되거나 stack의 top 원소가 h보다 커질 때까지 pop
            stack.pop()
            if not stack or stack[-1] > h:
                break
        stack.append(h)
print(len(stack))
    

# # 오른쪽부터 순회하면서 더 높은 것만 +1
# import sys

# N = int(sys.stdin.readline())
# arr = [int(sys.stdin.readline()) for _ in range(N)]
# ans = 1
# max_h = arr[N-1]
# for i in range(N-1, -1, -1):
#     if arr[i] > max_h:
#         max_h = arr[i]
#         ans += 1
# print(ans)