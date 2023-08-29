# # 풀이 2. [시간 초과] (딕셔너리 안 쓰고는 어려운 듯) 이분탐색
# import sys; input = sys.stdin.readline

# def binary_search(key):
#     s = 0
#     e = N-1
#     while s <= e:
#         mid = (s+e) // 2
#         if numbers[mid] == key:
#             return numbers[s:e+1].count(key)
#         elif numbers[mid] > key:
#             e = mid - 1
#         else:
#             s = mid + 1
    
#     return -1


# N = int(input())
# numbers = list(map(int, input().split()))
# numbers.sort()

# M = int(input())
# keys = list(map(int, input().split()))
# for key in keys:
#     # 이분탐색
#     # key의 index 찾기
#     i = binary_search(key)
#     if i == -1:
#         print(0, end=' ')
#     else:
#         print(i, end=' ')


# 풀이 1. [정답] [820ms] 딕셔너리 이용
import sys; input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dic = {}
for n in numbers:   # O(N)
    dic[n] = dic.get(n, 0) + 1

M = int(input())
key = list(map(int, input().split()))
for k in key:       # O(M)
    print(dic.get(k, 0), end=' ')   # O(1)