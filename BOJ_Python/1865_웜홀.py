import sys; input = sys.stdin.readline

def bellman_ford():
    times = [0] * (N + 1)

    for i in range(N):
        for v in range(1, N + 1):
            for nv, t in adj_d[v].items():
                if times[nv] > times[v] + t:
                    times[nv] = times[v] + t
                    if i == N - 1:
                        return 'YES'

    return 'NO'


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    adj_d = [{} for _ in range(N + 1)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        adj_d[S][E] = min(adj_d[S].get(E, T), T)
        adj_d[E][S] = min(adj_d[E].get(S, T), T)
    for _ in range(W):
        S, E, T = map(int, input().split())
        T = -T
        adj_d[S][E] = min(adj_d[S].get(E, T), T)

    print(bellman_ford())