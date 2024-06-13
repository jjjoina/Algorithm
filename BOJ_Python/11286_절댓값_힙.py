import sys; input = sys.stdin.readline
import heapq
from collections import deque

pq = []

N = int(input())
for _ in range(N):
    o = int(input())

    if o == 0:
        if pq:
            n = heapq.heappop(pq)
            if n != int(n):
                n = -(int(n) + 1)
            print(n)
        else:
            print(0)
            
    else:
        if o < 0:
            o = -o - 0.5
        heapq.heappush(pq, o)