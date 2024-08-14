import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
T, *truth = list(map(int, input().split()))

people_by_party = [[]]
party_by_person = [[] for _ in range(N + 1)]

for i in range(1, M + 1):
    n, *people = list(map(int, input().split()))
    people_by_party.append(people)
    for person in people:
        party_by_person[person].append(i)

q = deque()
party_can_lie = [True] * (M + 1)

for person in truth:
    for party in party_by_person[person]:
        q.append(party)
        party_can_lie[party] = False

while q:
    p = q.popleft()
    for person in people_by_party[p]:
        for party in party_by_person[person]:
            if party_can_lie[party]:
                q.append(party)
                party_can_lie[party] = False

print(party_can_lie.count(True) - 1)