import sys; input = sys.stdin.readline
sys.setrecursionlimit(200000)

def dfs(v):
    sheep = 0
    for w in prev[v]:
        sheep += dfs(w)

    if islands[v][0] == 'W':
        return max(sheep - islands[v][1], 0)
    else:
        return sheep + islands[v][1]


N = int(input())
islands = [[], ['W', 0]]
prev = [[] for _ in range(N+1)]
for i in range(2, N+1):
    t, a, p = input().split()
    islands.append([t, int(a)])
    prev[int(p)].append(i)

print(dfs(1))