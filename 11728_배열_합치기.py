# 풀이 2. 투 포인터
import sys; input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i = j = 0
ans = []
while i < N and j < M:
    if A[i] < B[j]:
        ans.append(A[i])
        i += 1
    else:
        ans.append(B[j])
        j += 1

if i == N:
    ans.extend(B[j:])
else:
    ans.extend(A[i:])

print(*ans)



# # 풀이 1. sort 메서드
# import sys; input = sys.stdin.readline

# N, M = map(int, input().split())
# lst = list(map(int, input().split())) + list(map(int, input().split()))

# lst.sort()

# print(*lst)