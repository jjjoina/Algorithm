word = input()
word = word.upper()
cnt = [0] * 26
for c in word:
    cnt[ord(c) - ord('A')] += 1
max_cnt = max(cnt)
ans = []
for i in range(26):
    if cnt[i] == max_cnt:
        ans.append(chr(i + ord('A')))
if len(ans) == 1:
    print(*ans)
else:
    print('?')    