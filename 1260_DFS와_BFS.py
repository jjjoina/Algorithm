import sys; input = sys.stdin.readline

# 정점 번호가 작은 것부터 방문

def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    for w in range(1, N+1):
        # 인접 and 방문하지 않았음
        if adj_m[v][w] and not visited[w]:
            dfs(w)


def bfs(v):
    q = [v]
    visited[v] = 1
    print(v, end=' ')

    while q:
        t = q.pop(0)
        for w in range(1, N+1):
            if adj_m[t][w] and not visited[w]:
                q.append(w)
                visited[w] = 1
                print(w, end=' ')


N, M, V = map(int, input().split())
adj_m = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

visited = [0] * (N+1)
dfs(V)
print()

visited = [0] * (N+1)
bfs(V)