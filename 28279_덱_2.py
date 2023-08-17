'''
11
6
1 3
1 8
7
8
3
2 5
1 2
5
4
4
'''

import sys; sys.stdin = open('28279_덱_2.py', encoding='utf-8')
input()

import sys; input = sys.stdin.readline
from collections import deque

deq = deque()

N = int(input())
for _ in range(N):
    c = input().split()
    
    if c[0] == '1':
        deq.appendleft(c[1])
    
    elif c[0] == '2':
        deq.append(c[1])
    
    elif c[0] == '3':
        if deq: print(deq.popleft())
        else: print(-1)

    elif c[0] == '4':
        if deq: print(deq.pop())
        else: print(-1)

    elif c[0] == '5':
        print(len(deq))

    elif c[0] == '6':
        if deq: print(0)
        else: print(1)

    elif c[0] == '7':
        if deq: print(deq[0])
        else: print(-1)

    elif c[0] == '8':
        if deq: print(deq[-1])
        else: print(-1)