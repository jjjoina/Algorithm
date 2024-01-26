while True:
    n = int(input())
    if n == -1: break

    divisors = []
    for i in range(1, n//2 + 1):
        if n % i == 0: divisors.append(i)
        
    if sum(divisors) == n:
        print(f'{n} = ', end='')
        print(*divisors, sep=' + ')
        # print(f'{n} = {divisors[0]}', end='')
        # for d in divisors[1:]:
        #     print(f' + {d}', end='')
        # print()
    else:
        print(f'{n} is NOT perfect.')