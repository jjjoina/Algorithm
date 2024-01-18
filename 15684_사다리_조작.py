import sys; input = sys.stdin.readline

def run():
    for l in range(N-1):    # N-1개 세로선만 내려가봐도 결과 나온다.
        j = l
        for i in range(H):
            if arr[i][j] != 0:  # 가로선 있으면
                j += arr[i][j]  # 이동
        
        if j != l:
            return False
        
    # for row in arr: print(row)
    return True


def comb(cur_depth, max_depth, start):
    global ans
    
    if cur_depth == max_depth:
        if run():
            ans = max_depth
        return
    
    for n in range(start, N*H):
        if ans != -1:
            return

        i, j = divmod(n, N)
        
        if j == N-1:    # 최우측 세로줄은 패스
            continue

        if arr[i][j] == 0 and arr[i][j+1] == 0: # 가로선을 놓을 수 있는 경우
            arr[i][j] = 1   # 가로선 설치
            arr[i][j+1] = -1
            comb(cur_depth+1, max_depth, n+1)
            arr[i][j] = arr[i][j+1] = 0     # 원복


N, M, H = map(int, input().split())
arr = [[0] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[a-1][b] = -1

ans = -1
for max_depth in range(4):
    comb(0, max_depth, 0)
print(ans)