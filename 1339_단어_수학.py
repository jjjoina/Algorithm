import sys; input = sys.stdin.readline

N = int(input())
lst = [input().strip() for _ in range(N)]

points = {}
for i in range(N):
    for c in lst[i]:
        points[c] = 0

for i in range(N):
    n = len(lst[i])
    for j in range(n):
        points[lst[i][j]] += 10 ** (n-j-1)

rst = list(points.items())
rst.sort(key=lambda x : -x[1])

ans = 0
for i in range(len(rst)):
    ans += rst[i][1] * (9-i)

print(ans)



# # 풀이 1. [시간 초과] 모든 순열 완전 탐색
# import sys; input = sys.stdin.readline

# def calculate():
#     global ans

#     dic = {}
#     for i in range(A):
#         dic[p[i]] = 9 - i

#     sum_v = 0
#     for i in range(N):
#         val = 0
#         for j in range(len(lst[i])):
#             val *= 10
#             val += dic[lst[i][j]]
#         sum_v += val
    
#     ans = max(ans, sum_v)


# def perm(i):
#     if i == A:
#         calculate()
#         return
    
#     for j in range(A):
#         if not used[j]:
#             p.append(alphabet_list[j])
#             used[j] = 1
#             perm(i+1)
#             p.pop()
#             used[j] = 0


# N = int(input())
# lst = [input().strip() for _ in range(N)]

# alphabet_set = set()
# for i in range(N):
#     for j in range(len(lst[i])):
#         alphabet_set.add(lst[i][j])

# alphabet_list = list(alphabet_set)
# A = len(alphabet_list)
# p = []
# used = [0] * A
# ans = 0

# perm(0)

# print(ans)