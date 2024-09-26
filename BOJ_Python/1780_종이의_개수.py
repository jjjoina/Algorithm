import sys; input = sys.stdin.readline

def recursive(si, sj, n):   
    for i in range(si, si + n):
        for j in range(sj, sj + n):
            if arr[si][sj] != arr[i][j]:
                for di in range(0, n, n // 3):
                    for dj in range(0, n, n // 3):
                        recursive(si + di, sj + dj, n // 3)
                return

    ans_lst[arr[si][sj] + 1] += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans_lst = [0, 0, 0]

recursive(0, 0, N)

for ans in ans_lst:
    print(ans)