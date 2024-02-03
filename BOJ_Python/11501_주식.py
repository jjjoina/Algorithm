import sys; input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    max_p = lst[N-1]
    
    for i in range(N-2, -1, -1):
        if max_p < lst[i]:
            max_p = lst[i]
        else:
            ans += max_p - lst[i]
    
    print(ans)