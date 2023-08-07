# 최대 21
# N장에 카드에서 3장을 고른다
# 3장의 합이 M 이하면서 최대
N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_v = 0
for i in range(N):
    for j in range(N):
        if j > i:
            for k in range(N):
                if k > j:
                    sum_v = cards[i] + cards[j] + cards[k]
                    if max_v < sum_v <= M:
                        max_v = sum_v

print(max_v)

# 다른 사람
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             ...