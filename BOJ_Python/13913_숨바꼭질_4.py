import sys; input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque([N])
    frm[N] = -2
    while q:
        v = q.popleft()
        for w in [v-1, v+1, 2*v]:
            if 0 <= w <= 100000 and frm[w] == -1:
                q.append(w)
                frm[w] = v
                if w == K:
                    return


N, K = map(int, input().split())

frm = [-1] * 100001

bfs()

ans = []
v = K
while v != -2:
    ans.append(v)
    v = frm[v]

print(len(ans) - 1)
print(*reversed(ans))