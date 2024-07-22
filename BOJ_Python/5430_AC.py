import sys; input = sys.stdin.readline
from collections import deque

def run():
    sign = True
    for f in functions:
        if f == 'R':
            sign = not sign
        else:
            if not dq:
                return 'error'

            if sign:
                dq.popleft()
            else:
                dq.pop()

    return f'[{",".join(dq if sign else reversed(dq))}]'


T = int(input())
for _ in range(T):
    functions = input().strip()
    n = int(input())
    s = input().strip('\n[]').split(',')
    dq = deque(s) if n else deque()

    print(run())