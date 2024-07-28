import math

N = int(input())

cnt = [0] * 10

while N > 0:
    cnt[N % 10] += 1
    N //= 10

cnt[6] = cnt[9] = math.ceil((cnt[6] + cnt[9]) / 2)

print(max(cnt))