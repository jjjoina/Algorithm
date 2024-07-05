# 풀이 3. [960ms] dp
import sys; input = sys.stdin.readline
sys.setrecursionlimit(1001)

def top_down(v):
    if finish_times[v] != -1:
        return
    
    finish_times[v] = D[v]
    for w in prev[v]:
        top_down(w)
        if finish_times[v] < finish_times[w] + D[v]:
            finish_times[v] = finish_times[w] + D[v]


for _ in range(int(input())):
    N, K = map(int, input().split())
    D = [None] + list(map(int, input().split()))
    prev = [[] for _ in range(N+1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        prev[Y].append(X)
    W = int(input())

    finish_times = [-1] * (N+1)

    top_down(W)
    
    print(finish_times[W])