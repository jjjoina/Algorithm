import sys; input = sys.stdin.readline
import heapq

T = int(input())
for _ in range(T):
    K = int(input())
    pq = list(map(int, input().split()))
    heapq.heapify(pq)
    
    ans = 0
    for _ in range(K-1):
        min1 = heapq.heappop(pq)
        min2 = heapq.heappop(pq)
        sum_ = min1 + min2
        ans += sum_
        heapq.heappush(pq, sum_)
    
    print(ans)