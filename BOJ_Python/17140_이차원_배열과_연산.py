import sys; input = sys.stdin.readline

MAX = 100

r, c, k = map(int, input().split())
r -= 1
c -= 1
arr = [[0] * MAX for _ in range(MAX)]
for i in range(3):
    arr[i][:3] = map(int, input().split())

ans = -1
time = 0

R = C = 3

while time < MAX + 1:
    # for row in arr: print(*row)
    # print()

    if arr[r][c] == k:
        ans = time
        break

    max_len = 0

    # 정렬하기
    if R >= C:
        for i in range(R):
            # 개수 세기
            dic = {}
            for j in range(C):
                if arr[i][j] == 0: continue
                dic[arr[i][j]] = dic.get(arr[i][j], 0) + 1        

            lst = sorted(dic.items(), key=lambda x: (x[1], x[0]))
            l = min(len(lst)*2, MAX)
            for j in range(l//2):
                arr[i][2*j] = lst[j][0]
                arr[i][2*j+1] = lst[j][1]
            
            # 0 채우기
            for j in range(MAX - l):
                arr[i][l+j] = 0

            if max_len < l:
                max_len = l
        
        C = max_len
        
    else:
        for j in range(C):
            # 개수 세기
            dic = {}
            for i in range(R):
                if arr[i][j] == 0: continue
                dic[arr[i][j]] = dic.get(arr[i][j], 0) + 1

            lst = sorted(dic.items(), key=lambda x: (x[1], x[0]))
            l = min(len(lst)*2, MAX)
            for i in range(l//2):
                arr[2*i][j] = lst[i][0]
                arr[2*i+1][j] = lst[i][1]

            # 0 채우기
            for i in range(MAX - l):
                arr[l+i][j] = 0

            if max_len < l:
                max_len = l
        
        R = max_len

    time += 1

print(ans)