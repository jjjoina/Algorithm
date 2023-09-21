import sys; input = sys.stdin.readline
import heapq

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(heap, x)
    else:
        if heap: print(heapq.heappop(heap))
        else: print(0)