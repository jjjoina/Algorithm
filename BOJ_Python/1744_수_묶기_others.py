import sys; input = sys.stdin.readline

less_than_1 = []
more_than_1 = []
ans = 0

N = int(input())
for _ in range(N):
    n = int(input())
    if n < 1:
        less_than_1.append(n)
    elif n > 1:
        more_than_1.append(n)
    else:
        ans += 1

less_than_1.sort(reverse=True)
more_than_1.sort()

while less_than_1:
    num1 = less_than_1.pop()
    if less_than_1:
        ans += num1 * less_than_1.pop()
    else:
        ans += num1
        break

while more_than_1:
    num1 = more_than_1.pop()
    if more_than_1:
        ans += num1 * more_than_1.pop()
    else:
        ans += num1
        break

print(ans)