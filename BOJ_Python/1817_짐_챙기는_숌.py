import sys; input = sys.stdin.readline

N, M = map(int, input().split())

if N == 0:
    print(0)
else:
    weights = list(map(int, input().split()))
    ans = 1
    left = M

    for w in weights:   # 마지막 상자에 담을 수 있는 경우
        if w <= left:
            left -= w
        else:           # 상자가 추가로 필요한 경우
            ans += 1
            left = M - w

    print(ans)