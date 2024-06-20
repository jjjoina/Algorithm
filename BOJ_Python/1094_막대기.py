import heapq

X = int(input())

pq = [64]
while sum(pq) > X:
    min_ = heapq.heappop(pq)
    min_ //= 2
    heapq.heappush(pq, min_)
    if sum(pq) < X:
        heapq.heappush(pq, min_)    

print(len(pq))