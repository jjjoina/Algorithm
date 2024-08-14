import sys; input = sys.stdin.readline

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])

    return parent[v]


def union(u, v):
    pu = find(u)
    pv = find(v)

    if pu < pv:
        parent[pv] = pu
    else:
        parent[pu] = pv


N, M = map(int, input().split())
_, *truth = list(map(int, input().split()))

parent = [i for i in range(N + 1)]

# 진실을 알고 있는 사람들은 0번 집합으로 묶는다.
for t in truth:
    parent[t] = 0

parties = []

for _ in range(M):
    n, *party = list(map(int, input().split()))

    parties.append(party)

    # 같은 파티에 속한 사람들을 같은 집합으로 묶는다.
    # 예를 들어 파티가 다음과 같이 2개 있다고 해보자.
    # (2, 5, 8), (1, 4, 5)
    # 파티 1을 순회하면서 2, 5, 8의 대표값이 모두 2로 설정된다.
    # 파티 2를 순회하면서 1, 4, 5의 대표값이 모두 1로 설정된다.
    # 5의 대표값이 2였으므로 2의 대표값이 1로 설정되고, 같은 원리로 파티 1의 모든 대표값이 1이 된다.
    # 두 파티에 공통 원소(5)가 있으므로 하나의 묶음이 된 것이다.
    # 묶음 안의 원소들은 항상 모두 같은 대표값을 갖는다.
    # 이후 한 원소의 대표값이 n으로 변경되면, 사실상 대표값(1)의 대표값(1)이 n으로 변경되는 것이므로,
    # 모든 원소들의 대표값이 n으로 된다. find(i) = find(n) = n

    for i in range(n - 1):
        union(party[i], party[i + 1])

ans = 0

for party in parties:
    if find(party[0]) != 0:
        ans += 1

print(ans)