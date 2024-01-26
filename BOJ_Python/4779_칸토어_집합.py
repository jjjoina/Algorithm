def recursive(s, i):
    if i == 0: return

    recursive(s, i-1)
    lst[s+3**(i-1):s+2*3**(i-1)] = [' '] * 3**(i-1)
    recursive(s+2*3**(i-1), i-1)


while True:
    try:
        N = int(input())
        lst = ['-'] * 3 ** N
        recursive(0, N)
        print(''.join(lst))
    except:
        break