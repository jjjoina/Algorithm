import sys; input = sys.stdin.readline

def is_possible(n):
    cnt = 1
    prev = 0

    for i in range(1, N):
        if lst[i] - lst[prev] < n:
            continue

        prev = i
        cnt += 1

        if cnt == C:
            return True

    return False


def binary_search():
    l = 0
    r = lst[-1] - lst[0]

    while l <= r:
        m = (l + r) // 2

        if is_possible(m):
            l = m + 1   # 더 큰 간격 시도
        else:
            r = m - 1

    return r


N, C = map(int, input().split())
lst = [int(input()) for _ in range(N)]

lst.sort()

print(binary_search())