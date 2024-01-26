# 풀이 2. [60ms] [다른 사람] 2번의 dijkstra
import sys; input = sys.stdin.readline
import heapq

def dijkstra(start, adj_l):
    heap = []
    W = [987654321] * (N+1)
    W[start] = 0
    heapq.heappush(heap, (W[start], start))

    while heap:
        w, v = heapq.heappop(heap)
        # 꺼내온 데이터가 현재 W보다 작거나 같으면 진행
        if w == W[v]:   # 등호여도 된다!
            # 인접한 정점들에 대해서
            for nv, d in adj_l[v]:
                dist = w + d
                if dist < W[nv]:
                    # 거기까지의 dist가 현재 W보다 작으면 갱신
                    W[nv] = dist
                    # 그리고 갱신한 정점에 한해 heappush
                    heapq.heappush(heap, (W[nv], nv))
    
    return W


# 마을의 수(= 학생의 수), 도로의 수(단방향), 파티 장소
N, M, X = map(int, input().split())
adj_l = [[] for _ in range(N+1)]
reverse_adj_l = [[] for _ in range(N+1)]
for _ in range(M):
    f, t, w = map(int, input().split())
    adj_l[f].append((t, w))         # from -> to 저장
    # 역방향 그래프를 함께 저장한다.
    reverse_adj_l[t].append((f, w)) # to -> from 저장


# X에서 각 집으로 돌아가는 시간 먼저 계산
to_home = dijkstra(X, adj_l)

# 각 집에서 X로 가는 것을 1번의 dijkstra로 계산!!
# HOW?? 역방향 그래프로 X에서 출발하는 것!!
home_to = dijkstra(X, reverse_adj_l)

ans = 0
for i in range(1, N+1):
    ans = max(ans, to_home[i] + home_to[i])

print(ans)



# # 풀이 1. [948ms] N번의 dijkstra
# import sys; input = sys.stdin.readline
# import heapq

# def dijkstra(start):
#     heap = []
#     W = [987654321] * (N+1)
#     W[start] = 0
#     heapq.heappush(heap, (W[start], start))

#     while heap:
#         w, v = heapq.heappop(heap)
#         # 꺼내온 데이터가 현재 W보다 작거나 같으면 진행
#         if w == W[v]:   # 등호여도 된다!
#             # 인접한 정점들에 대해서
#             for nv, d in adj_l[v]:
#                 dist = w + d
#                 if dist < W[nv]:
#                     # 거기까지의 dist가 현재 W보다 작으면 갱신
#                     W[nv] = dist
#                     # 그리고 갱신한 정점에 한해 heappush
#                     heapq.heappush(heap, (W[nv], nv))
    
#     return W


# # 마을의 수(= 학생의 수), 도로의 수(단방향), 파티 장소
# N, M, X = map(int, input().split())
# adj_l = [[] for _ in range(N+1)]
# for _ in range(M):
#     f, t, w = map(int, input().split())
#     adj_l[f].append((t, w))


# # X에서 각 집으로 돌아가는 시간 먼저 계산
# to_home = dijkstra(X)

# ans = 0
# for start in range(1, N+1):
#     if start != X:
#         W = dijkstra(start)
#         ans = max(ans, W[X] + to_home[start])

# print(ans)