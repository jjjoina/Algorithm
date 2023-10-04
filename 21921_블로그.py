import sys; input = sys.stdin.readline

N, X = map(int, input().split())
lst = list(map(int, input().split()))

max_v = visitors = sum(lst[:X])
cnt = 1

for i in range(1, N-X+1):
    visitors = visitors - lst[i-1] + lst[i+X-1]
    if max_v < visitors:
        max_v = visitors
        cnt = 1
    elif max_v == visitors:
        cnt += 1

if max_v == 0:
    print('SAD')
else:
    print(max_v)
    print(cnt)