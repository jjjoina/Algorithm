N = int(input())
lst = list(map(int, input().split()))

ys = 0
ms = 0

for t in lst:
    ys += (t // 30 + 1) * 10
    ms += (t // 60 + 1) * 15

if ys < ms:
    print(f'Y {ys}')
elif ys > ms:
    print(f'M {ms}')
else:
    print(f'Y M {ys}')