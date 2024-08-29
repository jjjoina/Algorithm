# 풀이 1. [151592KB, 1640ms] 이분 탐색, 유니온 파인드
import sys; input = sys.stdin.readline

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(u, v):
    pu = find(u)
    pv = find(v)
    if pu < pv:
        parent[pu] = pv
    else:
        parent[pv] = pu


def binary_search(weight):
    l = 0
    r = len_bags - 1

    while l <= r:
        m = (l + r) // 2
        if bags[m][0] < weight:
            l = m + 1
        else:
            r = m - 1

    return l


N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bag_cnt = {}
for _ in range(K):
    c = int(input())
    bag_cnt[c] = bag_cnt.get(c, 0) + 1

jewels.sort(key=lambda x: -x[1])    # 가격 내림차순 정렬
bags = [[c, cnt] for c, cnt in bag_cnt.items()]
bags.sort(key=lambda x: x[0])

len_bags = len(bags)
parent = [i for i in range(len_bags + 1)]
ans = 0

for weight, price in jewels:
    i = binary_search(weight)
    pi = find(i)

    if pi < len_bags:  # 담을 수 있는 경우
        ans += price
        bags[pi][1] -= 1

        if bags[pi][1] == 0:
            union(pi, pi + 1)

print(ans)