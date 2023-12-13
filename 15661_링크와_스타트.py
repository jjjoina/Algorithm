import sys; input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 987654321

for i in range(2**(N-1)-1): # i번째 팀의 경우
    t0 = []
    t1 = []
    for j in range(N-1):    # j번 사람
        if i & (1<<j) == 0:
            t0.append(j)
        else:
            t1.append(j)
    t1.append(N-1)

    # t0의 능력치의 합
    sum0 = 0
    for a in t0:
        for b in t0:
            sum0 += arr[a][b]

    # t1의 능력치의 합
    sum1 = 0
    for a in t1:
        for b in t1:
            sum1 += arr[a][b]
        if sum1 - sum0 >= ans:
            break

    ans = min(ans, abs(sum0-sum1))

print(ans)