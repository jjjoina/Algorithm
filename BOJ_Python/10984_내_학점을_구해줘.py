import sys; input = sys.stdin.readline

for _ in range(int(input())):
    sum_c = 0
    sum_g = 0
    
    N = int(input())
    for _ in range(N):
        C, G = map(float, input().split())
        sum_c += C
        sum_g += G * C
        
    print(f'{sum_c:.0f} {sum_g / sum_c:.1f}')