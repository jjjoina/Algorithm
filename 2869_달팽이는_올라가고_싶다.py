A, B, V = map(int, input().split())
ans = (V-A) // (A-B)
if (V-A) % (A-B):
    ans += 1
print(ans + 1)