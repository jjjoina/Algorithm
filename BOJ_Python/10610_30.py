import sys; input = sys.stdin.readline

numbers = sorted(map(int, input().strip()), reverse=True)

if numbers[-1] != 0:
    print(-1)
else:
    sum_ = 0
    for number in numbers:
        sum_ += number

    if sum_ % 3 != 0:
        print(-1)
    else:
        print(''.join(map(str, numbers)))