import sys; input = sys.stdin.readline
from collections import deque

def is_tree(start, visited):
    q = deque()
    q.append([start, -1])
    visited[start] = True
    result = True

    while q:
        v, pv = q.popleft()

        for nv in adj_l[v]:
            if nv == pv:
                continue

            if visited[nv]:
                result = False
            else:
                q.append([nv, v])
                visited[nv] = True

    return result


def count_trees():
    visited = [False] * (n + 1)
    cnt = 0

    for i in range(1, n + 1):
        if not visited[i]:
            if is_tree(i, visited):
                cnt += 1

    return cnt


tc = 1
answer = []

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    adj_l = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        adj_l[u].append(v)
        adj_l[v].append(u)

    t = count_trees()

    if t == 0:
        s = 'No trees.'
    elif t == 1:
        s = 'There is one tree.'
    else:
        s = f'A forest of {t} trees.'

    answer.append(f'Case {tc}: {s}')

    tc += 1

print('\n'.join(answer))