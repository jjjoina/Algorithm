# 풀이 3. [268ms] Kruskal
import sys; input = sys.stdin.readline

def find_set(x):
    if parents[x] == x: return x
    
    parents[x] = find_set(parents[x])
    return parents[x]


def kruskal(start):
    cnt = 0         # 고른 간선의 개수
    sum_weight = 0  # 고른 간선들의 합
    for edge in edges:  # 가중치 작은 간선부터 순차적으로 채택
        f, t, w = edge
        # f와 t가 같은 집합인지 검사
        f = find_set(f)     # f <- f의 대표자
        t = find_set(t)     # t <- t의 대표자
        if f != t:          # 다른 집합이면 진행
            sum_weight += w     # 간선 채택
            cnt += 1            # 고른 간선 수 +1
            parents[t] = f      # 두 집합 병합
            
            if cnt == V-1:
                return sum_weight   # 간선 V-1개 골랐으면 종료


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])  # 가중치 기준으로 간선 정렬
parents = [i for i in range(V+1)]

print(kruskal(1))



# # 풀이 2. [420ms] Prim with heapq
# import sys; input = sys.stdin.readline
# import heapq

# def prim(start):
#     visited = [0] * (V+1)
#     sum_weight = 0
#     heap = []
#     heapq.heappush(heap, (0, start))

#     while heap:
#         weight, v = heapq.heappop(heap)
#         if not visited[v]:
#             visited[v] = 1
#             sum_weight += weight
#             for w, n_weight in adj_l[v]:
#                 if not visited[w]:
#                     heapq.heappush(heap, (n_weight, w))
    
#     return sum_weight


# V, E = map(int, input().split())
# adj_l = [[] for _ in range(V+1)]    # idx 0 미사용
# for _ in range(E):
#     A, B, C = map(int, input().split())
#     adj_l[A].append((B, C))
#     adj_l[B].append((A, C))

# print(prim(1))



# # 풀이 1. [시간 초과] Prim with for loop
# import sys; input = sys.stdin.readline

# def prim(start):
#     W[start] = 0
    
#     for _ in range(V):
#         # 1. 방문하지 않은 정점들 중 가중치가 최소인 정점 찾기
#         min_w = int(1e10)
#         for i in range(1, V+1):
#             if not visited[i] and min_w > W[i]:
#                 min_w = W[i]
#                 v = i
        
#         # 2. 방문 체크
#         visited[v] = 1
        
#         # 3. 인접한 정점 중 방문하지 않은 정점의 가중치 갱신
#         for w, weight in adj_l[v]:
#             if not visited[w]:
#                 W[w] = min(W[w], weight)
        

# V, E = map(int, input().split())
# adj_l = [[] for _ in range(V+1)]
# for _ in range(E):
#     A, B, C = map(int, input().split())
#     adj_l[A].append((B, C))
#     adj_l[B].append((A, C))
    
# visited = [0] * (V+1)
# W = [0] + [int(1e10)] * V
# prim(1)
# print(sum(W))