A, B, C = map(int, input().split())

B_bit = []

while B > 0:
    B_bit.append(B % 2)
    B //= 2

ans = 1

for bit in reversed(B_bit):
    ans *= ans
    if bit == 1:
        ans *= A
    ans %= C

print(ans)