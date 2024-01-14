import sys; input = sys.stdin.readline

for _ in range(int(input())):
    P, M = map(int, input().split())

    seats = [0] * (M+1)
    ans = 0

    for _ in range(P):
        n = int(input())
        
        if seats[n] == 0:
            seats[n] += 1
        else:
            ans += 1
    
    print(ans)