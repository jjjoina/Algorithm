import sys; input = sys.stdin.readline

def rotate(t, d):
    dirr = [0] * T
    dirr[t] = d

    for i in range(t-1, -1, -1):
        if arr[i][2] != arr[i+1][6]:
            dirr[i] = -dirr[i+1]
        else:
            break

    for i in range(t+1, T):
        if arr[i][6] != arr[i-1][2]:
            dirr[i] = -dirr[i-1]
        else:
            break
    
    for i in range(T):
        if dirr[i] == 1:
            arr[i] = arr[i][7:] + arr[i][:7]
        elif dirr[i] == -1:
            arr[i] = arr[i][1:] + arr[i][:1]


T = int(input())
arr = [list(map(int, input().strip())) for _ in range(T)]
K = int(input())

for _ in range(K):
    n, d = map(int, input().split())
    rotate(n-1, d)

ans = 0
for i in range(T):
    if arr[i][0] == 1:
        ans += 1
print(ans)