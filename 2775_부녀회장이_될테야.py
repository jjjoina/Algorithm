# 아래층부터 올라가며 검사
T = int(input())
for t in range(1, T+1):
    k = int(input())    # 층
    n = int(input())    # 호
    arr = [[0] * (n+1) for _ in range(k+1)]

    # 0층 채우기
    for i in range(n+1):
        arr[0][i] = i
    # 1층 이상 채우기
    for i in range(1, k+1):
        for j in range(n+1):
            arr[i][j] += sum(arr[i-1][:j+1])
    
    print(arr[k][n])