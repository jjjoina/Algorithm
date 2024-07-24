import sys; input = sys.stdin.readline
import heapq

N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]

lectures.sort(key=lambda x: x[1])
pq = []
cnt = 0

for p, d in lectures:    # d 순방향
    heapq.heappush(pq, p)
    cnt += 1
    if cnt > d:
        heapq.heappop(pq)
        cnt -= 1

print(sum(pq))