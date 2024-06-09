import sys; input = sys.stdin.readline

while True:
    N = int(input())
    
    if N == 0:
        break

    sum_ = int(input())
    ans = sum_

    for _ in range(N-1):
        P = int(input())
        
        if sum_ > 0:
            sum_ += P
        else:
            sum_ = P

        if ans < sum_:
            ans = sum_

    print(ans)