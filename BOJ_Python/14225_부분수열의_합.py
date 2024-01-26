import sys; input = sys.stdin.readline

def perm(i, cur_sum):
    if i == N:
        rst.add(cur_sum)
        return
    
    perm(i+1, cur_sum)          # S[i] 미포함
    perm(i+1, cur_sum + S[i])   # S[i] 포함


N = int(input())
S = list(map(int, input().split()))

rst = set()
perm(0, 0)

ans = 1
while ans in rst:
    ans += 1
    
print(ans)