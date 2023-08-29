# 호수 = N-1을 H로 나눈 몫 + 1
# 층수 = H으로 나눈 나머지, 만약 0이면 H

T = int(input())
for t in range(1, T+1):
    H, W, N = map(int, input().split())
    floor = N % H
    if floor == 0: floor = H
    ans = (floor * 100) + ((N-1)//H + 1)
    print(ans)