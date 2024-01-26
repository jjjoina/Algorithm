import sys; input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}
for _ in range(N):
    w = input().rstrip()
    if len(w) >= M:
        dic[w] = dic.get(w, 0) + 1

lst = list(dic.items())
lst.sort(key=lambda x : (-x[1], -len(x[0]), x[0]))

for e in lst:
    print(e[0])