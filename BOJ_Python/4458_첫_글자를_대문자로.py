import sys; input = sys.stdin.readline

for _ in range(int(input())):
    s = list(input().strip())
    s[0] = s[0].upper()
    print(''.join(s))