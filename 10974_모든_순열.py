N = int(input())

def dfs(i):
    if i == N:
        print(*p)
        return
    
    for j in range(1, N+1):
        if used[j] == 0:
            p.append(j)
            used[j] = 1
            dfs(i+1)
            p.pop()
            used[j] = 0


used = [0] * (N+1)
p = []

dfs(0)