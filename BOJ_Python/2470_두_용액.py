import sys; input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

lst.sort()

l, r = 0, N-1
ans_sum = abs(lst[l] + lst[r])
ans_min = lst[l]
ans_max = lst[r]

while l < r:
    sum_ = lst[l] + lst[r]

    if ans_sum > abs(sum_):
        ans_sum = abs(sum_)
        ans_min = lst[l]
        ans_max = lst[r]

    if sum_ < 0:
        l += 1
    elif sum_ > 0:
        r -= 1
    else:
        ans_min = lst[l]
        ans_max = lst[r]
        break

print(ans_min, ans_max)