arr = [int(input()) for _ in range(5)]
# Bubble Sort
for i in range(4):
    for j in range(4-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

sum_v = 0
for num in arr:
    sum_v += num

print(sum_v // 5)
print(arr[2])