import sys; input = sys.stdin.readline

def dfs(depth, arr):
    global ans

    if depth == 5:
        # print('------------')
        # for row in arr: print(*row)
        for i in range(N):
            for j in range(N):
                if ans < arr[i][j]:
                    ans = arr[i][j]
        return

    # 좌
    a = []
    for i in range(N):
        lst = []
        cur = -1
        for j in range(N):
            if arr[i][j] == 0:  # 빈 칸인 경우
                continue
            if cur == -1:
                cur = arr[i][j]
            elif arr[i][j] == cur:  # 합쳐지는 경우
                lst.append(cur*2)
                cur = -1
            else:
                lst.append(cur)
                cur = arr[i][j]
        if cur != -1:   # 다 훑었는데 cur에 남아있는 경우
            lst.append(cur)
        
        lst = lst + [0] * (N - len(lst))
        a.append(lst)
    
    dfs(depth+1, a)

    # 우
    a = []
    for i in range(N):
        lst = []
        cur = -1
        for j in range(N-1, -1, -1):
            if arr[i][j] == 0:  # 빈 칸인 경우
                continue
            if cur == -1:
                cur = arr[i][j]
            elif arr[i][j] == cur:  # 합쳐지는 경우
                lst.append(cur*2)
                cur = -1
            else:
                lst.append(cur)
                cur = arr[i][j]
        if cur != -1:   # 다 훑었는데 cur에 남아있는 경우
            lst.append(cur)
        
        lst.reverse()
        lst = [0] * (N - len(lst)) + lst
        a.append(lst)
    
    dfs(depth+1, a)

    # 상
    a = []
    for j in range(N):
        lst = []
        cur = -1
        for i in range(N):
            if arr[i][j] == 0:  # 빈 칸인 경우
                continue
            if cur == -1:
                cur = arr[i][j]
            elif arr[i][j] == cur:  # 합쳐지는 경우
                lst.append(cur*2)
                cur = -1
            else:
                lst.append(cur)
                cur = arr[i][j]
        if cur != -1:   # 다 훑었는데 cur에 남아있는 경우
            lst.append(cur)
        
        lst = lst + [0] * (N - len(lst))
        a.append(lst)
    a = list(map(list, zip(*a)))

    dfs(depth+1, a)

    # 하
    a = []
    for j in range(N):
        lst = []
        cur = -1
        for i in range(N-1, -1, -1):
            if arr[i][j] == 0:  # 빈 칸인 경우
                continue
            if cur == -1:
                cur = arr[i][j]
            elif arr[i][j] == cur:  # 합쳐지는 경우
                lst.append(cur*2)
                cur = -1
            else:
                lst.append(cur)
                cur = arr[i][j]
        if cur != -1:   # 다 훑었는데 cur에 남아있는 경우
            lst.append(cur)

        lst.reverse()
        lst = [0] * (N - len(lst)) + lst
        a.append(lst)
    a = list(map(list, zip(*a)))

    dfs(depth+1, a)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0

dfs(0, arr)

print(ans)