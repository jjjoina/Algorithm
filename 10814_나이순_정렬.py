import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    arr.append([age, name])
arr.sort(key=lambda x: x[0])
for info in arr:
    print(*info)