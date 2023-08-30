N = int(input())
for i in range(1, 2*N):
    print(' ' * abs(N-i) + '*' * (2*N-1 - 2*abs(N-i)))