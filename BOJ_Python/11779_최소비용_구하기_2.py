# 풀이 2. [60468KB] [336ms] [다른 사람] 이전 노드 저장하는 리스트 도입
import sys; input = sys.stdin.readline
import heapq;

def dijkstra():
    W = [987654321] * (n+1)
    W[s] = 0
    heap = [[W[s], s]]
    
    while heap:
        dist, v = heapq.heappop(heap)
        
        if dist > W[v]:
            continue
        
        for w, weight in edges[v]:
            if W[w] > dist + weight:
                W[w] = dist + weight
                heapq.heappush(heap, [W[w], w])
                prev[w] = v
    
    return W[e]


n = int(input())
m = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    f, t, w = map(int, input().split())
    edges[f].append([t, w])
s, e = map(int, input().split())

prev = [-1] * (n+1)

ans_weight = dijkstra()
route = []
while e != -1:
    route.append(e)
    e = prev[e]

print(ans_weight)
print(len(route))
print(*route[::-1])


# # 풀이 1. [68636KB] [404ms] heapq에 현재까지의 경로 모두 저장
# import sys; input = sys.stdin.readline
# import heapq;

# def dijkstra():
#     W = [987654321] * (n+1)
#     W[s] = 0
#     heap = [[W[s], [s]]]
    
#     while heap:
#         dist, route = heapq.heappop(heap)
#         v = route[-1]
        
#         if dist > W[v]:
#             continue
        
#         for w, weight in edges[v]:
#             if W[w] > dist + weight:
#                 W[w] = dist + weight
#                 heapq.heappush(heap, [W[w], route + [w]])
#                 if w == e:
#                     rst_weight = W[w]
#                     rst_route = route + [w]
    
#     return rst_weight, rst_route


# n = int(input())
# m = int(input())
# edges = [[] for _ in range(n+1)]
# for _ in range(m):
#     f, t, w = map(int, input().split())
#     edges[f].append([t, w])
# s, e = map(int, input().split())

# ans_weight, ans_route = dijkstra()

# print(ans_weight)
# print(len(ans_route))
# print(*ans_route)