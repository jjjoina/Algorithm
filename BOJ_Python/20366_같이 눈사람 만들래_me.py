import sys; input = sys.stdin.readline

def is_possible(*radius_lst):
    tmp_dict = {}
    for r in radius_lst:
        tmp_dict[r] = tmp_dict.get(r, 0) + 1

    for r, cnt in tmp_dict.items():
        if cnt_dict[r] < cnt:
            return False

    return True


N = int(input())
lst = list(map(int, input().split()))

cnt_dict = {}
for r in lst:
    cnt_dict[r] = cnt_dict.get(r, 0) + 1

combinations = []
for i in range(N-1):
    for j in range(i+1, N):
        combinations.append([lst[i]+lst[j], lst[i], lst[j]])
combinations.sort()

ans = 10 ** 10
for i in range(len(combinations)-1):
    if ans > combinations[i+1][0] - combinations[i][0]:
        if is_possible(*combinations[i+1][1:], *combinations[i][1:]):
            ans = combinations[i+1][0] - combinations[i][0]

print(ans)