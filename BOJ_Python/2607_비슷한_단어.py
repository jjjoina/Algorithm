import sys; input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]

std = [0] * 26
for c in words[0]:
    std[ord(c) - ord('A')] += 1

ans = 0
for word in words[1:]:
    cnt = [0] * 26
    for c in word:
        cnt[ord(c) - ord('A')] += 1

    diff = [std[i] - cnt[i] for i in range(26)]
    cnt1 = cnt0 = cnt_1 = 0
    for i in range(26):
        if diff[i] == 1: cnt1 += 1
        elif diff[i] == 0: cnt0 += 1
        elif diff[i] == -1: cnt_1 += 1
    
    if (cnt0 == 26)\
        or ((cnt1 == 1 or cnt_1 == 1) and cnt0 == 25)\
        or (cnt1 == 1 and cnt_1 == 1 and cnt0 == 24):
        ans += 1

print(ans)