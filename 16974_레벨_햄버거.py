def burger(lv, si):
    global ans

    if lv == 0:
        ans += 1
        return

    if X == si:
        # ans += 0
        return
    elif X == si + (BP[lv]-1)//2:
        ans += P[lv-1] + 1
        return
    elif X == si + BP[lv] - 1:
        ans += P[lv]
        return
    
    if X < si + (BP[lv]-1)//2:
        # ans += 0
        burger(lv-1, si+1)
    else:
        ans += P[lv-1] + 1
        burger(lv-1, si+(BP[lv]-1)//2+1)


N, X = map(int, input().split())
X -= 1      # 인덱스 맞추기

BP = [1] + [0] * N
P = [1] + [0] * N
for i in range(1, N+1):
    BP[i] = BP[i-1]*2 + 3
    P[i] = P[i-1]*2 + 1

ans = 0

burger(N, 0)

print(ans)