n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())

n = n1 * d2 + n2 * d1
d = d1 * d2

# 기약분수화
a, b = max(n, d), min(n, d)
while b > 0:
    a, b = b, a%b
gcd = a
n //= gcd
d //= gcd
print(n, d)