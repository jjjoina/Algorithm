import sys; input = sys.stdin.readline

def dfs(i, prev):
    if i == M:
        tpl = tuple(p)
        if tpl not in s:
            s.add(tpl)
            print(*p)
        return

    for j in range(prev+1, N-M+i+1):
        p.append(lst[j])
        dfs(i+1, j)
        p.pop()


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

p = []
s = set()

dfs(0, -1)