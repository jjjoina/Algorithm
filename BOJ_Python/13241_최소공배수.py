ori_A, ori_B = map(int, input().split())
A, B = max(ori_A, ori_B), min(ori_A, ori_B)
while B > 0:
    A, B = B, A%B
gcd = A
lcm = ori_A * ori_B // gcd
print(lcm)