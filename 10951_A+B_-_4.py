# 풀이 2. try-except 이용

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break


# # 풀이 1. readlines 이용

# import sys;

# arr = sys.stdin.readlines()
# for i in range(len(arr)):
#     A, B = map(int, arr[i].split())
#     print(A+B)