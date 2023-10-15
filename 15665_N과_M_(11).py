import sys; input = sys.stdin.readline

def dfs(i):
    if i == M:
        print(*p)
        return
    
    for j in range(N):
        p.append(lst[j])
        dfs(i+1)
        p.pop()


N, M = map(int, input().split())
lst = sorted(list(set(map(int, input().split()))))

N = len(lst)
p = []

dfs(0)