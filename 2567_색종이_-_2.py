import sys; input = sys.stdin.readline

arr = [[0] * 101 for _ in range(101)]
N = int(input())

# 색종이 붙이기
for _ in range(N):
    r, c = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            arr[i][j] = 1

ans = 0 
for i in range(100):
    for j in range(100):
        if arr[i][j]:
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni, nj = i+di, j+dj
                # 범위를 벗어나는 경우
                if not (0 <= ni < 101) or not (0 <= nj < 101):
                    ans += 1
                # 1에서 4방향 탐색했을 때 0과 만나는 경우
                if arr[ni][nj] == 0:
                    ans += 1

print(ans)