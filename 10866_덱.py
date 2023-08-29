# 풀이 2. [76ms] [얘가 더 느리다?!] deque 사용
import sys; input = sys.stdin.readline
from collections import deque

N = int(input())
d = deque()
for _ in range(N):
    c = input().split()
    if c[0] == 'push_front':
        d.appendleft(c[1])
    elif c[0] == 'push_back':
        d.append(c[1])
    elif c[0] == 'pop_front':
        if d: print(d.popleft())
        else: print(-1)
    elif c[0] == 'pop_back':
        if d: print(d.pop())
        else: print(-1)
    elif c[0] == 'size':
        print(len(d))
    elif c[0] == 'empty':
        if d: print(0)
        else: print(1)
    elif c[0] == 'front':
        if d: print(d[0])
        else: print(-1)
    elif c[0] == 'back':
        if d: print(d[-1])
        else: print(-1)


# # 풀이 1. [52ms] deque 미사용
# import sys; input = sys.stdin.readline

# N = int(input())
# d = []
# for _ in range(N):
#     c = input().split()
#     if c[0] == 'push_front':
#         d.insert(0, c[1])
#     elif c[0] == 'push_back':
#         d.append(c[1])
#     elif c[0] == 'pop_front':
#         if d: print(d.pop(0))
#         else: print(-1)
#     elif c[0] == 'pop_back':
#         if d: print(d.pop())
#         else: print(-1)
#     elif c[0] == 'size':
#         print(len(d))
#     elif c[0] == 'empty':
#         if d: print(0)
#         else: print(1)
#     elif c[0] == 'front':
#         if d: print(d[0])
#         else: print(-1)
#     elif c[0] == 'back':
#         if d: print(d[-1])
#         else: print(-1)