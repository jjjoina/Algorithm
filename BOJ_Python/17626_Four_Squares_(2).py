# 풀이 2. [48ms] DP

def solve():
    if is_square[N]:
        return 1
    
    for i in range(1, int(N**0.5) + 1):
        if is_square[N - i**2]:
            return 2
    
    for i in range(1, int(N**0.5) + 1):
        for j in range(1, int((N - i**2) ** 0.5) + 1):
            if is_square[N - i**2 - j**2]:
                return 3
            
    return 4


N = int(input())

is_square = [False] * (N+1)
for i in range(1, int(N**0.5) + 1):
    is_square[i**2] = True

print(solve())