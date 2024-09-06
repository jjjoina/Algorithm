import sys; input = sys.stdin.readline
sys.setrecursionlimit(200000)

def dfs(v):
    if current_visited[v]:  # 싸이클 발견
        return v

    current_visited[v] = True

    cycle_start_v = -1

    if not global_visited[nv[v]]:
        cycle_start_v = dfs(nv[v])

        if cycle_start_v != -1:
            global ans
            ans -= 1

            if cycle_start_v == v:
                cycle_start_v = -1

    current_visited[v] = False
    global_visited[v] = True

    return cycle_start_v


T = int(input())
for _ in range(T):
    n = int(input())
    nv = [0] + list(map(int, input().split()))

    global_visited = [False] * (n + 1)
    current_visited = [False] * (n + 1)
    ans = n

    for start in range(1, n + 1):
        if not global_visited[start]:
            dfs(start)

    print(ans)