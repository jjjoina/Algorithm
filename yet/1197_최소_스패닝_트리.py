import sys; input = sys.stdin.readline

def prim(start):
    W[start] = 0
    
    for _ in range(V):
        # 1. 방문하지 않은 정점들 중 가중치가 최소인 정점 찾기
        min_w = int(1e10)
        for i in range(1, V+1):
            if not visited[i] and min_w > W[i]:
                min_w = W[i]
                v = i
        
        # 2. 방문 체크
        visited[v] = 1
        
        # 3. 인접한 정점 중 방문하지 않은 정점의 가중치 갱신
        for w, weight in adj_l[v]:
            if not visited[w]:
                W[w] = min(W[w], weight)
        

V, E = map(int, input().split())
adj_l = [[] for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    adj_l[A].append((B, C))
    adj_l[B].append((A, C))
    
visited = [0] * (V+1)
W = [0] + [int(1e10)] * V
prim(1)
print(sum(W))