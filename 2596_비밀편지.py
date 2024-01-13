import sys; input = sys.stdin.readline

def decrypt(code):
    for j in range(8):
        compare = [code[k] == table[j][k] for k in range(6)]
        if compare.count(False) <= 1:
            return chr(ord('A') + j)
    
    return False


N = int(input())
lst = list(map(int, input().strip()))

table = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0]
]

ans = ''
for i in range(N):
    rst = decrypt(lst[i*6:(i+1)*6])

    if rst == False:
        ans = i + 1
        break
    else:
        ans += rst

print(ans)