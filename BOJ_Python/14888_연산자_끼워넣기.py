import sys; input = sys.stdin.readline

def calculate():
    global ans_max, ans_min

    rst = A[0]
    for i in range(N-1):
        if p[i] == 0:
            rst += A[i+1]
        elif p[i] == 1:
            rst -= A[i+1]
        elif p[i] == 2:
            rst *= A[i+1]
        else:
            if rst < 0 and A[i+1] > 0:
                rst = -(-rst // A[i+1])
            else:
                rst //= A[i+1]
            
    if ans_max < rst: 
        ans_max = rst
    if ans_min > rst:
        ans_min = rst


def perm():
    if len(p) == N-1:
        calculate()
        return
    
    for i in range(4):
        if operator_cnt[i] > 0:
            p.append(i)
            operator_cnt[i] -= 1
            perm()
            p.pop()
            operator_cnt[i] += 1


N = int(input())
A = list(map(int, input().split()))
operator_cnt = list(map(int, input().split()))

p = []
ans_max = -9876543210
ans_min = 9876543210

perm()

print(ans_max)
print(ans_min)