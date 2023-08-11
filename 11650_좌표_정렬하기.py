# 둘 다 정답

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[0], x[1]))
for c in arr:
    print(*c)

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# arr.sort()
# for c in arr:
#     print(*c)