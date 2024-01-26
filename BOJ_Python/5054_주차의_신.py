import sys; input = sys.stdin.readline

for _ in range(int(input())):

    n = int(input())
    lst = list(map(int, input().split()))
    
    max_v, min_v = max(lst), min(lst)
    ans = 2 * (max(lst) - min(lst))
    
    print(ans)