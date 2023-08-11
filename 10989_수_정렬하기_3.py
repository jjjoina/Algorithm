import sys
cnt = [0] * 10001
N = int(input())
for _ in range(N):
    cnt[int(sys.stdin.readline())] += 1
for i in range(10001):
    for _ in range(cnt[i]):
        print(i)