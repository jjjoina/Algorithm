def dfs(n):
    if len(n) == 1:
        global ans
        ans += 1
        return

    dfs(n[:-1])
    if n[:-1] != n[1:]:
        dfs(n[1:])


N = input()

ans = 0

dfs(N)

print(ans)