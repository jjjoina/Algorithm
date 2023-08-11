N, K = map(int, input().split())
arr = list(range(1, N+1))
p = 0
ans = []
while N > 0:
    p = (p + (K-1)) % N
    ans.append(str(arr.pop(p)))
    N -= 1
print(f'<{", ".join(ans)}>')