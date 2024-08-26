import sys; input = sys.stdin.readline

groups = [[] for _ in range(5)]

N = int(input())
for _ in range(N):
    n = int(input())
    if n < -1:
        groups[0].append(n)
    elif n == -1:
        groups[1].append(n)
    elif n == 0:
        groups[2].append(n)
    elif n == 1:
        groups[3].append(n)
    else:
        groups[4].append(n)

groups[0].sort(reverse=True)
groups[4].sort()

ans = 0

while len(groups[0]) >= 2:
    ans += groups[0].pop() * groups[0].pop()

if groups[0]:
    if groups[1]:
        ans += groups[0].pop() * groups[1].pop()
    elif groups[2]:
        ans += groups[0].pop() * groups[2].pop()
    else:
        ans += groups[0].pop()

while len(groups[1]) >= 2:
    ans += groups[1].pop() * groups[1].pop()

if groups[1]:
    if groups[2]:
        ans += groups[1].pop() * groups[2].pop()
    else:
        ans += groups[1].pop()

while len(groups[4]) >= 2:
    ans += groups[4].pop() * groups[4].pop()

if groups[4]:
    ans += groups[4].pop()

while groups[3]:
    ans += groups[3].pop()

print(ans)