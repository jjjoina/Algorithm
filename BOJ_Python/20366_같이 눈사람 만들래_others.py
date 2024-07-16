import sys; input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

combinations = []
for i in range(N-1):
    for j in range(i+1, N):
        combinations.append([lst[i]+lst[j], i, j])
combinations.sort()

ans = 10 ** 10
for i in range(len(combinations)-1):
    if ans > combinations[i+1][0] - combinations[i][0]:
        if len({*combinations[i+1][1:], *combinations[i][1:]}) == 4:
            ans = combinations[i+1][0] - combinations[i][0]

print(ans)