import sys; input = sys.stdin.readline

def bt(i, w):
    global ans

    if i == N:
        ans += 1 
        return
    
    for j in range(N):
        if used[j] == 0:
            nw = w + A[j] - K
            if nw >= 500:
                used[j] = 1
                bt(i+1, nw)
                used[j] = 0


N, K = map(int, input().split())
A = list(map(int, input().split()))

used = [0] * N
ans = 0

bt(0, 500)

print(ans)