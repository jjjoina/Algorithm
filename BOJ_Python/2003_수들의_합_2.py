import sys; input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

s = f = 0
sum_v = lst[0]
ans = 0

while True:
    if sum_v <= M:
        if sum_v == M:
            ans += 1
        f += 1  # 피연산자 수 증가
        if f == N:
            break
        sum_v += lst[f]

    else:
        sum_v -= lst[s]
        s += 1  # 피연산자 수 감소

print(ans)