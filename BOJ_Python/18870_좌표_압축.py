# # X`i : Xi보다 작은 Xj의 개수
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
new_arr = list(set(arr))
new_arr.sort()
n_dict = {}
for i in range(len(new_arr)):
    n_dict[new_arr[i]] = i
for n in arr:
    print(n_dict[n], end=' ')