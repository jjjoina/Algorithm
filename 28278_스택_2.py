'''
9
4
1 3
1 5
3
2
5
2
2
5
'''

import sys; sys.stdin = open('28278_스택_2.py', encoding='utf-8')
input()

import sys; input = sys.stdin.readline

stack = []

N = int(input())
for _ in range(N):
    c = input().split()
    
    if c[0] == '1':
        stack.append(c[1])

    elif c[0] == '2':
        if stack: print(stack.pop())
        else: print(-1)

    elif c[0] == '3':
        print(len(stack))
        
    elif c[0] == '4':
        if stack: print(0)
        else: print(1)

    elif c[0] == '5':
        if stack: print(stack[-1])
        else: print(-1)