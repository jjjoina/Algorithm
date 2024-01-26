# 풀이 2. 이분탐색
import sys; input = sys.stdin.readline

# K : 이미 가지고 있는 랜선의 개수 / N : 필요한 랜선의 개수
K, N = map(int, input().split())
# 이미 가지고 있는 랜선들
arr = [int(input()) for _ in range(K)]

# 이분탐색
s = min(arr)//N
e = 2**31 - 1
while True:
    mid = (s+e)//2
    can_make = 0
    for i in range(K):
        can_make += arr[i]//mid
    if can_make >= N:
        next_make = 0   # 길이가 mid+1이면 만들 수 있는 개수
        for i in range(K):
            next_make += arr[i]//(mid+1)
        if next_make < N:
            ans = mid
            break
        else:   # 짧게 잡아서 많이 만들 수 있었구나
            s = mid + 1
    else:       # N개를 만들지 못함. 길게 잡았었구나
        e = mid - 1

print(ans)



# # 풀이 1. [역시 시간 초과] 브루트 포스
# import sys; input = sys.stdin.readline

# # K : 이미 가지고 있는 랜선의 개수 / N : 필요한 랜선의 개수
# K, N = map(int, input().split())
# # 이미 가지고 있는 랜선들
# arr = [int(input()) for _ in range(K)]

# for L in range(sum(arr)//N, -1, -1):
#     can_make = 0
#     for i in range(K):
#         can_make += arr[i]//L
#     if can_make >= N:
#         ans = L
#         break

# print(ans)