# 풀이 2. [44ms]
import sys; input = sys.stdin.readline

try:
    while True:
        n = int(input())

        ans = 1
        m = 1 % n

        while m:
            m = (m * 10 + 1) % n
            ans += 1

        print(ans)

except:
    pass



# # 풀이 1. [156ms]
# import sys; input = sys.stdin.readline

# try:
#     while True:
#         n = int(input())

#         ans = 1
#         m = 1

#         while m % n:
#             m = m * 10 + 1
#             ans += 1

#         print(ans)

# except:
#     pass