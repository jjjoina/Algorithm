import sys; input = sys.stdin.readline

s = list(input().strip())   # string
b = list(input().strip())    # bomb

S = len(s)
B = len(b)

rst = []
for i in range(S):
    rst.append(s[i])
    while rst[-B:] == b:
        for _ in range(B):
            rst.pop()

if rst: print(''.join(rst))
else:   print('FRULA')