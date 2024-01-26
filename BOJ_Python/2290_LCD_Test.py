import sys; input = sys.stdin.readline

s, n = input().split()
s = int(s)

r = s + 2
c = 2 * s + 3
N = len(n)
arr = [[' '] * (r*N + N-1) for _ in range(c)]

j = 0
for d in n:
    if d == '1':
        for i in range(1, c-1):
            if i == c//2:
                continue
            arr[i][j+r-1] = '|'
    
    elif d == '2':
        arr[0][j+1:j+r-1] = arr[c//2][j+1:j+r-1] = arr[c-1][j+1:j+r-1] = ['-'] * (r-2)
        for i in range(1, c//2):
            arr[i][j+r-1] = '|'
        for i in range(c//2+1, c-1):
            arr[i][j] = '|'

    elif d == '3':
        arr[0][j+1:j+r-1] = arr[c//2][j+1:j+r-1] = arr[c-1][j+1:j+r-1] = ['-'] * (r-2)
        for i in range(1, c-1):
            if i == c//2:
                continue
            arr[i][j+r-1] = '|'

    elif d == '4':
        for i in range(1, c//2):
            arr[i][j] = '|'
        arr[c//2][j+1:j+r-1] = ['-'] * (r-2)
        for i in range(1, c-1):
            if i == c//2:
                continue
            arr[i][j+r-1] = '|'
        
    elif d == '5':
        arr[0][j+1:j+r-1] = arr[c//2][j+1:j+r-1] = arr[c-1][j+1:j+r-1] = ['-'] * (r-2)
        for i in range(1, c//2):
            arr[i][j] = '|'
        for i in range(c//2+1, c-1):
            arr[i][j+r-1] = '|'
        
    elif d == '6':
        arr[0][j+1:j+r-1] = arr[c//2][j+1:j+r-1] = arr[c-1][j+1:j+r-1] = ['-'] * (r-2)
        for i in range(1, c-1):
            if i == c//2:
                continue
            arr[i][j] = '|'
        for i in range(c//2+1, c-1):
            arr[i][j+r-1] = '|'
    
    elif d == '7':
        arr[0][j+1:j+r-1]= ['-'] * (r-2)
        for i in range(1, c-1):
            if i == c//2:
                continue
            arr[i][j+r-1] = '|'
        
    elif d == '8':
        arr[0][j+1:j+r-1] = arr[c//2][j+1:j+r-1] = arr[c-1][j+1:j+r-1] = ['-'] * (r-2)
        for i in range(1, c-1):
            if i == c//2:
                continue
            arr[i][j] = arr[i][j+r-1] = '|'

    elif d == '9':
        arr[0][j+1:j+r-1] = arr[c//2][j+1:j+r-1] = arr[c-1][j+1:j+r-1] = ['-'] * (r-2)
        for i in range(1, c//2):
            arr[i][j] = '|'
        for i in range(1, c-1):
            if i == c//2:
                continue
            arr[i][j+r-1] = '|'
    
    else:
        arr[0][j+1:j+r-1] = arr[c-1][j+1:j+r-1] = ['-'] * (r-2)
        for i in range(1, c-1):
            if i == c//2:
                continue
            arr[i][j] = arr[i][j+r-1] = '|'
    
    j += r + 1

for row in arr:
    print(''.join(row))