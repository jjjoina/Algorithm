def digit(n):
    if n == 0:
        return 1, {0}
    
    cnt = 0
    s = set()
    
    while n > 0:
        s.add(n % 10)
        cnt += 1
        n //= 10
    
    return cnt, s


def solve():
    if M == 10:
        return abs(N - 100)
    
    ans1 = abs(N - 100)
    
    down = up = N
    while True:
        if down >= 0:
            d_len, d_set = digit(down)
            if d_set.issubset(buttons):
                ans2 = d_len + (N - down)
                break
            down -= 1

        u_len, u_set = digit(up)
        if u_set.issubset(buttons):
            ans2 = u_len + (up - N)
            break
        up += 1
    
    return min(ans1, ans2)


buttons = set(range(10))
N = int(input())
M = int(input())
if M > 0:
    broken = set(map(int, input().split()))
    buttons.difference_update(broken)

print(solve())