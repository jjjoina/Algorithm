# 100 x 100 도화지
# 10 x 10 검은색 색종이들

arr = [[0] * 100 for _ in range(100)]
N = int(input())
for _ in range(N):
    i, j = map(int, input().split())
    # i, 99-j ~ i+10, 99-j-10
    for row in range(i, i+10):
        for col in range(99-j, 89-j, -1):
            arr[row][col] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j]:
            ans += 1

print(ans)