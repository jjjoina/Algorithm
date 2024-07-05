# 풀이 2. [1084ms] 위상 정렬
import sys; input = sys.stdin.readline
from collections import deque

def find_start_buildings():     # 시작 건물들 찾기 (BFS)
    buildings = []
    q = deque()
    visited = [False] * (N+1)
    
    q.append(W)
    visited[W] = True
    
    while q:
        v = q.popleft()
        if prev[v]:
            for w in prev[v]:
                if not visited[w]:
                    q.append(w)
                    visited[w] = True
        else:
            buildings.append(v)
            finish_times[v] = D[v]
    
    return buildings


def build():    # 건물 짓기 (위상 정렬)    
    while buildings:
        v = buildings.pop()
        for w in next[v]:
            if finish_times[w] < finish_times[v] + D[w]:
                finish_times[w] = finish_times[v] + D[w]
            prev[w].pop()   # 진입차수 1 감소
            if not prev[w]:
                if w == W:
                    return
                buildings.append(w)


for _ in range(int(input())):
    N, K = map(int, input().split())
    D = [None] + list(map(int, input().split()))
    next = [[] for _ in range(N+1)]
    prev = [[] for _ in range(N+1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        next[X].append(Y)
        prev[Y].append(X)
    W = int(input())

    finish_times = [0] * (N+1)
    
    buildings = find_start_buildings()
    build()
    
    print(finish_times[W])