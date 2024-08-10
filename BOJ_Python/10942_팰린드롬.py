'''
set   -> 335248KB, 3296ms
array -> 61960KB,  1744ms
'''

import sys; input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

ans_m = [[0] * N for _ in range(N)]
# ans_set = set()

for i in range(N):
    # 중앙이 lst[i]인 팰린드롬
    l = i
    r = i

    while l >= 0 and r < N and lst[l] == lst[r]:
        ans_m[l][r] = 1
        # ans_set.add((l, r))
        l -= 1
        r += 1

    # 중앙이 lst[i], lst[i + 1]인 팰린드롬
    l = i
    r = i + 1

    while l >= 0 and r < N and lst[l] == lst[r]:
        ans_m[l][r] = 1
        # ans_set.add((l, r))
        l -= 1
        r += 1

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(ans_m[S - 1][E - 1])
    # print(1 if (S - 1, E - 1) in ans_set else 0)