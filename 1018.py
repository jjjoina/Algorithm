# M*N -> 8*8
# i j 설정
# in_i, in_j : range(8)
# 첫 칸이 B인 경우 바뀌게 되는 칸 수의 합, 최소값 갱신
# 첫 칸이 W인 경우 바뀌게 되는 칸 수의 합, 최소값 갱신
W = 'WBWBWBWB'
B = 'BWBWBWBW'

M, N = map(int, input().split())
arr = [input() for _ in range(M)]
ans = 64
for i in range(M-8+1):
    for j in range(N-8+1):
        # X_cnt : 첫 칸이 X인 체스판이 되기 위해 바꿔야하는 칸 수
        W_cnt = B_cnt = 0
        for in_i in range(8):
            for in_j in range(8):
                # 해당 칸과 B의 같은 위치와의 차이가 날 때마다
                if arr[i+in_i][j+in_j] != B[in_j]:
                    if in_i % 2:    # 홀수 행
                        W_cnt += 1
                    else:           # 짝수 행
                        B_cnt += 1
                # 해당 칸과 W의 같은 위치와의 차이가 날 때마다
                if arr[i+in_i][j+in_j] != W[in_j]:
                    if in_i % 2:    # 홀수 행
                        B_cnt += 1
                    else:           # 짝수 행
                        W_cnt += 1
        # print('(i, j)', i, j, '\t(W_cnt, B_cnt)', W_cnt, B_cnt)
        ans = min(W_cnt, B_cnt, ans)

print(ans)