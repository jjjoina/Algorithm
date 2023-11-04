import sys; input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

temp = []
ans = [-1]

for i in range(N-1, 0, -1):
    temp.append(lst[i])
    if lst[i-1] > lst[i]:
        for j in range(N-i):
            if temp[j] < lst[i-1]:
                temp[j], lst[i-1] = lst[i-1], temp[j]
                ans = lst[:i] + temp
                break
        break

print(*ans)