# 풀이 2. [118740KB, 1056ms] 우선순위 큐
import sys; input = sys.stdin.readline
import heapq

N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort(key=lambda x: -x[0])    # 보석을 무게 내림차순으로 정렬. 가벼운 보석부터 pop하며 보기 위함.
bags.sort()                         # 가방을 용량 오름차순으로 정렬. 까다로운 가방부터 보기 위함.
                                    # 10짜리 가방에 넣을 수 있는 보석이면 10 이상의 어떤 가방에도 넣을 수 있음을 이용.

prices = []    # 최대 힙. 가방에 담을 수 있는 보석의 가격들
ans = 0

for bag in bags:    # 용량 적은 가방부터 순회
    while jewels and jewels[-1][0] <= bag:  # 가장 가벼운 보석(가장 오른쪽에 있는 보석)을 가방에 넣을 수 있는 경우
        heapq.heappush(prices, -jewels[-1][1])  # 가격을 prices에 기록해둔다.
                                                # 비싼 것부터 pop할 것이므로, 즉 최대 힙이므로 음수로 push해둔다.
        jewels.pop()    # 다음으로 가벼운 보석을 보기 위해 리스트에서 제외한다.

    if prices:  # 가방에 담을 수 있는 보석이 있는 경우
        ans += -heapq.heappop(prices)   # 가장 비싼 가격의 보석을 담는다. (최대 힙에서 pop)

print(ans)