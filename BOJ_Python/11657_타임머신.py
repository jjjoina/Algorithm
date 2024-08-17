import sys; input = sys.stdin.readline

MAX = 10_000_000

def bellman_ford():
    weights = [MAX] * (N + 1)
    weights[1] = 0

    for i in range(1, N + 1):
        for A, B, C in edges:
            if weights[A] != MAX and weights[B] > weights[A] + C:
                weights[B] = weights[A] + C
                if i == N:
                    print(-1)   # N번째 반복에서 업데이트되었다면 음의 싸이클이 존재한다는 것
                    return

    for v in range(2, N + 1):
        print(weights[v] if weights[v] != MAX else -1)


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

bellman_ford()