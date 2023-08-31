import sys; input = sys.stdin.readline

N, B = input().split()
B = int(B)

ans = 0
e = 1
for i in range(len(N)):
    d = N[len(N)-1-i]
    if d.isdigit():
        d = int(d)
    else:
        d = ord(d) - ord('A') + 10
    ans += d * e
    e *= B

print(ans)