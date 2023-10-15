import sys; input = sys.stdin.readline

def dfs(i, prev):
    if i == M:
        print(*p)
        return
    
    for j in range(N):
        p.append(lst[j])
        dfs(i+1, j)
        p.pop()


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

p = []

dfs(0, 0)