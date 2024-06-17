import sys; input = sys.stdin.readline
import heapq

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    infections = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        infections[b].append([a, s])
    
    pq = [[0, c]]
    infected = [False] * (n+1)
    ans_cnt = 0
    
    while pq:
        t, v = heapq.heappop(pq)
        
        if infected[v]:
            continue
        
        infected[v] = True
        ans_cnt += 1
        ans_time = t
        
        for w, tt in infections[v]:
            # 이 코드가 dijkstra가 아닌 이유
            # 새로운 경로가 더 짧은 경로이든 긴 경로이든 일단 enqueue한다.
            # 때문에 메모리적으로 효율적이지 못하다.
            # 허나, 이 문제를 푸는 데 문제가 되지는 않는다.
            heapq.heappush(pq, [t+tt, w])
    
    print(ans_cnt, ans_time)