import math

for tc in range(int(input())):
    T, X = map(float, input().split())
    

    X = math.radians(X)
    t, s = math.tan(X), math.sin(X)
    period = 85 / t
    d = 16 / s

    while T >= period:
        T -= period

    if d >= period / 2: print('yes')
    else:
        if d <= T <= (period-d): print('yes')
        else: print('no')