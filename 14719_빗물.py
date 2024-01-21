import sys; input = sys.stdin.readline

H, W = map(int, input().split())
arr = [[0] * W for _ in range(H)]
lst = list(map(int, input().split()))
for j in range(W):
    for i in range(H-1, H-1-lst[j], -1):
        arr[i][j] = 1

ans = 0
for i in range(H):
    counting = False
    cnt = 0
    for j in range(W-1):
        if not counting:
            if arr[i][j] == 1 and arr[i][j+1] == 0:
                counting = True
        else:
            cnt += 1
            if arr[i][j+1] == 1:
                ans += cnt
                cnt = 0
                counting = False

print(ans)