import sys; input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

A.sort()

ans = 0
for m in range(1, N-1):
    l = m - 1
    r = m + 1
    while l >= 0 and r < N:
        if A[l] + A[r] < -A[m]:
            r += 1
            
        elif A[l] + A[r] > -A[m]:
            l -= 1
            
        else:
            cnt_l = 1
            cnt_r = 1
            
            while l-1 >= 0 and A[l-1] == A[l]:
                l -= 1
                cnt_l += 1
                
            while r+1 < N and A[r+1] == A[r]:
                r += 1
                cnt_r += 1
                
            ans += cnt_l * cnt_r
            
            l -= 1
            r += 1

print(ans)