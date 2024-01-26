# 풀이 2. 스택
T = int(input())
for t in range(1, T+1):
    stack = input().split()
    print(f'Case #{t}: ', end='')
    while stack:
        print(stack.pop(), end=' ')
    print()

# T = int(input())
# for t in range(1, T+1):
#     words = input().split()
#     print(f'Case #{t}:', *words[::-1])