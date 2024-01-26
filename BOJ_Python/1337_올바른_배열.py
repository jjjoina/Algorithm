import sys; input = sys.stdin.readline

# 풀이 2. 정렬 후 idx의 범위 이용
N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()  # O(NlogN)

max_v = 0
for i in range(N):  # O(N)
    m = 0
    for d in range(1, 5):
        # idx 범위 벗어남 방지
        if i+d < N and arr[i+d] < arr[i] + 5:
            m += 1
    if max_v < m: max_v = m
print(4 - max_v)



# # 풀이 1. set 이용 (in 연산 시간복잡도 O(1))
# 풀이 3. list 이용 (in 연산 시간복잡도 O(N))
N = int(input())
arr = [int(input()) for _ in range(N)]
arr = set(arr)

max_v = 0
for n in arr:   # O(N)
    m = 0
    for d in range(1, 5):
        if n+d in arr:  # set면 O(1) / list면 O(N)
            m += 1
    if max_v < m: max_v = m

print(4 - max_v)