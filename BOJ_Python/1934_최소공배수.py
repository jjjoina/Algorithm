# 풀이 2. [128ms] 유클리드 호제법

for _ in range(int(input())):
    ori_A, ori_B = map(int, input().split())
    A, B = max(ori_A, ori_B), min(ori_A, ori_B)
    while B > 0:
        A, B = B, A%B
    gcd = A
    lcm = ori_A * ori_B // gcd
    print(lcm)



# # 풀이 1. [168ms] 유클리드 호제법 X
# import math

# for _ in range(int(input())):
#     A, B = map(int, input().split())
#     dA = set()
#     dB = set()
#     for i in range(1, int(math.sqrt(A))+1):
#         if A % i == 0:
#             dA.add(i)
#             dA.add(A//i)
#     for i in range(1, int(math.sqrt(B))+1):
#         if B % i == 0:
#             dB.add(i)
#             dB.add(B//i)
#     gcd = max(dA & dB)
#     lcm = A * B // gcd
#     print(lcm)