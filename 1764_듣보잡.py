# 풀이 2. set 이용
import sys; input = sys.stdin.readline

N, M = map(int, input().split())
dj = set()
bj = set()
for _ in range(N):
    dj.add(input().rstrip())
for _ in range(M):
    bj.add(input().rstrip())

dbj = list(dj & bj)
dbj.sort()
print(len(dbj))
for name in dbj:
    print(name)



# 풀이 1. [시간 초과] O(n2)
# import sys; input = sys.stdin.readline

# N, M = map(int, input().split())
# dj = [input().rstrip() for _ in range(N)]
# bj = [input().rstrip() for _ in range(M)]

# dbj = []
# for i in range(M):
#     if bj[i] in dj:
#         dbj.append(bj[i])

# dbj.sort()
# l = len(dbj)
# print(l)
# for i in range(l):
#     print(dbj[i])