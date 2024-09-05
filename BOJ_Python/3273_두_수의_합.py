import sys; input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()

left = 0
right = n - 1
answer = 0

while left < right:
    sum_ = a[left] + a[right]

    if sum_ < x:
        left += 1
    elif sum_ > x:
        right -= 1
    else:
        answer += 1
        left += 1
        right -= 1

print(answer)