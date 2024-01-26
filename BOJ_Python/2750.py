N = int(input())
arr = [int(input()) for _ in range(N)]
# Selection Sort
for i in range(N-1):
    min_idx = i
    for j in range(i, N):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

for v in arr:
    print(v)