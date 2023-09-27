import sys; input = sys.stdin.readline

def find_head():
    # 머리 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '*':
                return i, j
            

N = int(input())
arr = [input().strip() for _ in range(N)]
hi, hj = find_head()
heart_i, heart_j = hi+1, hj

ans = [0] * 5

for j in range(heart_j-1, -1, -1):
    if arr[heart_i][j] == '*':
        ans[0] += 1
    else: break

for j in range(heart_j+1, N):
    if arr[heart_i][j] == '*':
        ans[1] += 1
    else: break

# 허리 끝점 찾기
for i in range(N-1, heart_i, -1):
    if arr[i][heart_j] == '*':
        waist_end_i = i
        break
ans[2] = waist_end_i - heart_i

for i in range(waist_end_i+1, N):
    if arr[i][heart_j-1] == '*':
        ans[3] += 1
    
    if arr[i][heart_j+1] == '*':
        ans[4] += 1

print(heart_i+1, heart_j+1)
print(*ans)