def dfs(i):
    # 부분집합에 lst[i] 포함 여부 결정
    global ans

    if i == N:
        if subset and sum(subset) == S: # 공집합인 경우 제외
            ans += 1
        return
    
    subset.append(lst[i])
    dfs(i+1)
    subset.pop()
    dfs(i+1)


N, S = map(int, input().split())
lst = list(map(int, input().split()))
subset = []
ans = 0

dfs(0)

print(ans)