import sys; input = sys.stdin.readline

book_cnt = {}

N = int(input())
for _ in range(N):
    title = input().strip()
    book_cnt[title] = book_cnt.get(title, 0) + 1

ans_cnt = 0
ans_title = ''
for title, cnt in book_cnt.items():
    if ans_cnt < cnt:
        ans_cnt = cnt
        ans_title = title
    elif ans_cnt == cnt and ans_title > title:
        ans_title = title

print(ans_title)