import sys; input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

i = 0
ans = 0

while i < M:
    if S[i] == 'I':
        l = i
        r = i+1
        target = 'O'

        while r < M:
            if S[r] == target:
                target = 'I' if target == 'O' else 'O'
                r += 1
            else:
                break

        cnt = (r-l-1) // 2 - N + 1
        if cnt > 0:
            ans += cnt

        i = r

    else:
        i += 1

print(ans)