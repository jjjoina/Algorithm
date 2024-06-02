import sys; input = sys.stdin.readline
import heapq

N = int(input())
pq = []
for _ in range(N):
    heapq.heappush(pq, int(input()))

ans = 0
while True:
    min1 = heapq.heappop(pq)
    if not pq:
        break
    min2 = heapq.heappop(pq)
    sum_ = min1 + min2
    ans += sum_
    heapq.heappush(pq, sum_)
    
print(ans)