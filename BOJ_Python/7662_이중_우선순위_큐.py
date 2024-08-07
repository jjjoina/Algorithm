import sys; input = sys.stdin.readline
import heapq

def insert(n):
    heapq.heappush(min_pq, n)
    heapq.heappush(max_pq, -n)


def clear(pq, del_cnt):
    while pq and del_cnt.get(pq[0], 0) > 0:
        del_cnt[pq[0]] -= 1
        heapq.heappop(pq)


def delete(n):
    if n == 1:  # 최대값 삭제
        clear(max_pq, max_pq_del_cnt)
        if max_pq:
            max_ = -heapq.heappop(max_pq)
            min_pq_del_cnt[max_] = min_pq_del_cnt.get(max_, 0) + 1

    else:       # 최소값 삭제
        clear(min_pq, min_pq_del_cnt)
        if min_pq:
            min_ = -heapq.heappop(min_pq)
            max_pq_del_cnt[min_] = max_pq_del_cnt.get(min_, 0) + 1


T = int(input())
for _ in range(T):
    min_pq = []
    max_pq = []
    min_pq_del_cnt = {}
    max_pq_del_cnt = {}

    k = int(input())
    for _ in range(k):
        c, n = input().split()
        if c == 'I':
            insert(int(n))
        else:
            delete(int(n))

    clear(min_pq, min_pq_del_cnt)
    clear(max_pq, max_pq_del_cnt)

    if not min_pq and not max_pq:
        print('EMPTY')
    else:
        print(-max_pq[0], min_pq[0])