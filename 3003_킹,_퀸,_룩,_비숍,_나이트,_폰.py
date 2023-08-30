normal = [1, 1, 2, 2, 2, 8]
current = list(map(int, input().split()))
ans = [normal[i] - current[i] for i in range(6)]
print(*ans)