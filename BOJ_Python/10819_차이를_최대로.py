def perm(i):
    global ans

    if i == N:
        # 계산
        rst = 0
        for k in range(N-1):
            rst += abs(p[k]-p[k+1])
        ans = max(ans, rst)
        return

    for j in range(N):
        if used[j] == 0:
            p.append(A[j])
            used[j] = 1
            perm(i+1)
            p.pop()
            used[j] = 0


N = int(input())
A = list(map(int, input().split()))

p = []
used = [0] * N
ans = 0

perm(0)

print(ans)