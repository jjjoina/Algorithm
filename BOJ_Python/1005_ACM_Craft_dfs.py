# 풀이 1. [시간 초과] dfs
import sys; input = sys.stdin.readline

def dfs(v, t):
    # 리프 노드에 다다르면 해당 노드의 인덱스를 leafs에 저장
    if not edges[v]:
        times[v] = max(times[v], t + D[v])   # 누적 시간 갱신
        leafs.add(v)
        return

    # 탐색하면서 누적 시간을 더 큰 것으로 갱신
    times[v] = max(times[v], t + D[v])
    
    for w in edges[v]:
        dfs(w, times[v])


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())            # 건물의 개수, 건설순서 규칙의 개수
    D = [0] + list(map(int, input().split()))   # 건물별 건설에 걸리는 시간
    edges = [[] for _ in range(N+1)]
    for _ in range(K):
        a, b = map(int, input().split())
        edges[b].append(a)  # edges[i] : i를 짓기 위해서 먼저 지어져야하는 건물 리스트
    W = int(input())        # 건설해야 할 건물의 번호

    times = [0] * (N+1)
    leafs = set()

    # 지어야할 최종 건물부터 탐색
    dfs(W, 0)

    # 모든 탐색이 끝나면 리프 노드들의 시간의 합 구하기
    ans = 0
    for i in leafs:
        ans += times[i]
    print(ans)