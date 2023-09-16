import sys; input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    n = int(input())

    dic = {}
    for _ in range(n):
        name, kind = input().split()
        dic[kind] = dic.get(kind, 0) + 1
        
    ans = 1
    for v in dic.values():
        ans *= (v+1)
    print(ans - 1)