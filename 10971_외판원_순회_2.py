import sys; input = sys.stdin.readline

def perm(i, cur_sum):
    global ans

    if cur_sum >= ans:  # 가지치기 - 이미 ans 이상인 경우
        return

    if i == N:
        if W[p[i-1]][p[0]] != 0:
            cur_sum += W[p[i-1]][p[0]]
            if ans > cur_sum:
                ans = cur_sum
        return
    
    for j in range(N):
        if used[j] == 0:
            if W[p[i-1]][j] != 0:    # 가지치기 - W가 0인 경우
                p.append(j)
                used[j] = 1
                perm(i+1, cur_sum+W[p[i-1]][j])
                p.pop()
                used[j] = 0


N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

ans = 987654321
used = [0] * N
p = []

for i in range(N):  # i : 첫 도시
    p.append(i)
    used[i] = 1
    perm(1, 0)
    p.pop()
    used[i] = 0

print(ans)