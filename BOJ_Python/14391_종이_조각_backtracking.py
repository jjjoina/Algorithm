import sys; input = sys.stdin.readline

def dfs(idx, cur_sum):
    if idx == N * M:
        global ans
        if ans < cur_sum:
            ans = cur_sum
            # print(log, ans)
        return
    
    rs, cs = divmod(idx, M)
    
    if used[rs][cs]:
        dfs(idx+1, cur_sum)
    
    else:
        used[rs][cs] = True
        
        # log.append(arr[rs][cs])
        dfs(idx+1, cur_sum+int(arr[rs][cs]))
        # log.pop()
        
        tmp = []

        s = arr[rs][cs]
        for ce in range(cs+1, M):
            if used[rs][ce]:
                break
            s += arr[rs][ce]
            used[rs][ce] = True
            tmp.append([rs, ce])
            # log.append(s)
            dfs(idx+1, cur_sum+int(s))
            # log.pop()
            # ce += 1
        while tmp:
            rt, ct = tmp.pop()
            used[rt][ct] = False
            
        s = arr[rs][cs]
        for re in range(rs+1, N):
            if used[re][cs]:
                break
            s += arr[re][cs]
            used[re][cs] = True
            tmp.append([re, cs])
            # log.append(s)
            dfs(idx+1, cur_sum+int(s))
            # log.pop()
            # re += 1
        while tmp:
            rt, ct = tmp.pop()
            used[rt][ct] = False

        used[rs][cs] = False


N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

used = [[False] * M for _ in range(N)]
ans = 0

# log = []
dfs(0, 0)

print(ans)