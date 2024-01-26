import sys; input = sys.stdin.readline

def dfs(depth, arr):
    global ans

    # 백트래킹
    max_v = 0
    for i in range(N):
        for j in range(N):
            if max_v < arr[i][j]:
                max_v = arr[i][j]
    if max_v * (2 ** (10-depth)) < ans:
        return

    if depth == 10:
        ans = max_v
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