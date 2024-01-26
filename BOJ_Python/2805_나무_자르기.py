import sys; input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

s = 0
e = max(lst)

while s <= e:
    m = (s+e) // 2

    rst = 0
    for t in lst:
        if t > m:
            rst += t - m

    if rst >= M:   # 나무를 덜 자를 수도 있는 경우
        s = m + 1

    else:   # 나무를 더 많이 잘라야 하는 경우
        e = m - 1
    
print(e)