A = int(input())
B = int(input())
C = int(input())
N = A * B * C
cnt = [0] * 10
for d in str(N):
    cnt[int(d)] += 1
for c in cnt:
    print(c)