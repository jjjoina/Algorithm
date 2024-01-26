n = int(input())

if n in [1, 2]:
    print(0)
else:
    ans = n * (n-1) * (n-2) // 6
    print(ans)

print(3)