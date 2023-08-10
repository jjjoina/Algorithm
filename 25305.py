# 내림차순 정렬했을 때 arr[k-1]
N, k = map(int, input().split())
arr = list(map(int, input().split()))

# 내림차순 정렬 (Bubble Sort)
for i in range(N-1):
    for j in range(N-1-i):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr[k-1])