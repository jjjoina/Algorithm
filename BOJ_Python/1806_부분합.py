import sys; input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))

s = f = 0
sum_v = lst[0]
ans = 987654321

while True:
    if f == N-1 and sum_v < S:  # 탐색 종료
        break

    if f - s + 1 >= ans:    # 길이가 현재 정답 이상인 경우
        s += 1
        sum_v -= lst[s-1]
        continue

    if sum_v >= S:
        ans = f - s + 1
        s += 1
        sum_v -= lst[s-1]

    else:
        f += 1
        sum_v += lst[f]

if ans == 987654321:
    ans = 0
print(ans)