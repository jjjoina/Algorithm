import sys; input = sys.stdin.readline

def choose(i, order):
    if lotto[i][order] == 0:
        if order == n - 1:
            lotto[i][order] = m - 2 * i + 1
        else:
            for j in range(2 * i, m // pow(2, n - order - 1) + 1):
                lotto[i][order] += choose(j, order + 1)

    return lotto[i][order]


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    if n == 1:
        answer = m
    else:
        lotto = [[0] * n for _ in range(m + 1)]
        answer = 0

        for i in range(1, m // pow(2, n - 1) + 1):
            answer += choose(i, 1)

    print(answer)