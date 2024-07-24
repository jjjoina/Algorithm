import sys; input = sys.stdin.readline
import heapq

N = int(input())
assignments = [list(map(int, input().split())) for _ in range(N)]

assignments_by_date = [[] for _ in range(1001)]
for d, w in assignments:
    assignments_by_date[d].append(w)
pq = []
ans = 0

for d in range(1000, 0, -1):
    for p in assignments_by_date[d]:
        heapq.heappush(pq, -p)

    if pq:
        ans += -heapq.heappop(pq)

print(ans)