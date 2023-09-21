# # 풀이 2. [시간 초과] Dijkstra with no heap
# def dijkstra(start):
#     T[start] = 0

#     for _ in range(100001*100001):
#         # 1. 방문하지 않은 정점 중 최소 시간인 정점 구하기
#         min_t = 987654321
#         for i in range(100001):
#             if not visited[i] and min_t > T[i]:
#                 min_t = T[i]
#                 v = i

#         # 2. 방문 체크
#         visited[v] = 1
#         # 중간에 K 찾으면 return??
#         if v == K: return

#         # 3. 인접한 정점의 시간 갱신
#         for w in [v-1, v+1]:
#             if 0 <= w <= 100000:
#                 T[w] = min(T[w], T[v] + 1)
        
#         if 0 <= 2*v <= 100000:
#             T[2*v] = min(T[2*v], T[v])


# N, K = map(int, input().split())
# visited = [0] * 100001
# T = [987654321] * 100001    # 각 정점에 도착하는 최소 시간
# dijkstra(N)
# print(T[K])



# # 풀이 1. [틀림] BFS
# from collections import deque

# N, K = map(int, input().split())
# visited = [-1] * 100001
# q = deque()
# q.append(N)

# # 시간 기록 (방문 체크)
# t = N
# while t <= 100000:
#     q.append(t)
#     visited[t] = 0 
#     t *= 2

# # BFS
# while q:
#     i = q.popleft()
#     for ni in [i-1, i+1]:
#         if 0 < ni <= 100000 and visited[ni] == -1:
#             t = ni
#             while t <= 100000:
#                 q.append(t)
#                 visited[t] = visited[i] + 1
#                 t *= 2

# if K == 0:
#     print(N)
# else:    
#     print(visited[K])