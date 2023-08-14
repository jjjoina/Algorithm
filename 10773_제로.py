import sys; input = sys.stdin.readline

# 딱 후입선출 -> 스택 문제로군

K = int(input())
stack = []
for _ in range(K):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))