import sys; input = sys.stdin.readline

S = input().strip()

lst = [S[i:] for i in range(len(S))]
lst.sort()

for s in lst:
    print(s)