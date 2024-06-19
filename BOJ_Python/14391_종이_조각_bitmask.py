import sys; input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

ans = 0

for b in range(1 << (N*M)):     # 비트마스킹
    sum_ = 0
    calculated = [[False] * M for _ in range(N)]

    for i in range(N*M):    # i번 비트
        r, c = divmod(i, M)
        
        if calculated[r][c]:
            continue
        
        partial_sum = arr[r][c]
        
        if b & (1<<i):  # 세로 묶음인 경우
            for rr in range(r+1, N):
                ii = rr * M + c
                if not b & (1<<ii):
                    break
                partial_sum = partial_sum * 10 + arr[rr][c]
                calculated[rr][c] = True
                
        else:           # 가로 묶음인 경우
            for cc in range(c+1, M):
                ii = r * M + cc
                if b & (1<<ii):
                    break
                partial_sum = partial_sum * 10 + arr[r][cc]
                calculated[r][cc] = True
        
        sum_ += partial_sum
        calculated[r][c] = True
    
    if ans < sum_:
        ans = sum_

print(ans)