def solution(n, m, x, y, r, c, k):
    x -= 1
    y -= 1
    r -= 1
    c -= 1

    min_route = []
    min_route.extend(['d' if x < r else 'u'] * abs(r - x))
    min_route.extend(['l' if y > c else 'r'] * abs(c - y))
    min_route.sort()
    min_route = ''.join(min_route)

    d = k - len(min_route)

    if d < 0 or d % 2 == 1:
        return 'impossible'

    down = min(d // 2, (n - 1) - max(x, r))
    d -= down * 2

    left = min(d // 2, min(y, c))
    d -= left * 2

    index = 0
    while index < len(min_route):
        if min_route[index] in ['r', 'u']:
            break
        index += 1

    answer = 'd' * down + min_route[:index] + 'l' * left + 'rl' * (d // 2) + 'r' * left + min_route[index:] + 'u' * down

    return answer