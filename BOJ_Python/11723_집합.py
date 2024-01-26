import sys; input = sys.stdin.readline

M = int(input())
s = set()
for _ in range(M):
    o = input().split()
    if len(o) == 2: o[1] = int(o[1])
    if o[0] == 'add':
        s.add(o[1])
    elif o[0] == 'remove':
        s.discard(o[1])
    elif o[0] == 'check':
        print(1 if o[1] in s else 0)
    elif o[0] == 'toggle':
        if o[1] in s: s.remove(o[1])
        else: s.add(o[1])
    elif o[0] == 'all':
        s = set(range(1, 21))
    elif o[0] == 'empty':
        s.clear()