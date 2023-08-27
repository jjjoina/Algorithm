lights = [0] + list(input())
N = len(lights)
ans = 0
for i in range(1, N):
    if lights[i] == 'Y':
        ans += 1
        for j in range(i, N, i):
            if lights[j] == 'Y': lights[j] = 'N'
            elif lights[j] == 'N': lights[j] = 'Y'

print(ans)