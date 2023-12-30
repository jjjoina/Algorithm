for _ in range(int(input())):
    n = int(input())
    cnt = 0
    
    while n > 0:
        bit = n % 2
        if bit == 1:
            print(cnt, end=' ')
        n //= 2
        cnt += 1
    
    print()