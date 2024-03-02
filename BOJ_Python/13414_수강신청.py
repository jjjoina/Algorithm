import sys; input = sys.stdin.readline

K, L = map(int, input().split())
stoi = {}
for i in range(L):
    s = input().strip()
    stoi[s] = i

rst = sorted(stoi.items(), key=lambda x: x[1])

N = min(K, len(rst))
for i in range(N):
    print(rst[i][0])