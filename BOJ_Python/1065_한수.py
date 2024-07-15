def is_hansoo(n):
    lst = list(map(int, str(n)))

    if len(lst) == 1:
        return True

    standard = lst[0] - lst[1]
    for i in range(1, len(lst)-1):
        if lst[i] - lst[i+1] != standard:
            return False

    return True


N = int(input())

ans = 0
for n in range(1, N+1):
    if is_hansoo(n):
        ans += 1

print(ans)