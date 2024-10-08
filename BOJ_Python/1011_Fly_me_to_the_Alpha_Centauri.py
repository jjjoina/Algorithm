'''
1 -> 1

2 -> 1 + 1

3 -> 1 + 1 + 1
4 -> 1 + 2 + 1

5 -> 1 + 2 + 1 + 1
6 -> 1 + 2 + 2 + 1

7 -> 1 + 2 + 1 + 2 + 1
8 -> 1 + 2 + 2 + 2 + 1
9 -> 1 + 2 + 3 + 2 + 1

10 -> 1 + 2 + 3 + 2 + 1 + 1
11 -> 1 + 2 + 3 + 2 + 2 + 1
12 -> 1 + 2 + 3 + 3 + 2 + 1

13 -> 1 + 2 + 3 + 3 + 2 + 1 + 1
14 -> 1 + 2 + 3 + 3 + 2 + 2 + 1
15 -> 1 + 2 + 3 + 3 + 3 + 2 + 1
16 -> 1 + 2 + 3 + 4 + 3 + 2 + 1

...
'''

import sys; input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())

    d = y - x
    l = 1
    r = 1 << 15

    while l <= r:
        m = (l + r) // 2

        if m * (m + 1) >= d:
            r = m - 1
        else:
            l = m + 1

    if d <= l * l:
        print(2 * l - 1)
    else:
        print(2 * l)