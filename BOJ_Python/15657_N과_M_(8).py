def dfs(i, prev):
    # i번째 원소 고르는 함수
    # prev : 지난번 선택해서 고른 idx
    if i == M:
        print(*rst)
        return
    
    for j in range(prev, N):
        rst.append(lst[j])
        dfs(i+1, j)
        rst.pop()


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

rst = []
dfs(0, 0)