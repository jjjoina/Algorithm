import sys; input = sys.stdin.readline
import heapq

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    infections = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        infections[b].append([a, s])
    
    pq = [[0, c]]
    infection_time = [987654321] * (n+1)
    infection_time[c] = 0
    
    while pq:
        t, v = heapq.heappop(pq)
        
        if t > infection_time[v]:
            continue
        
        for w, tt in infections[v]:
            nt = t + tt
            if nt < infection_time[w]:
                # dijkstra의 특징
                # 새로운 경로가 더 짧은 경로일 때만 enqueue한다.
                heapq.heappush(pq, [nt, w])
                infection_time[w] = nt

    # ans_cnt = 0
    # ans_time = 0
    # for t in infection_time:
    #     if t == 987654321:
    #         continue
    #     ans_cnt += 1
    #     if ans_time < t:
    #         ans_time = t
    
    # 제너레이터
    ans_cnt = sum(1 for t in infection_time if t != 987654321)
    ans_time = max(t for t in infection_time if t != 987654321)

    print(ans_cnt, ans_time)