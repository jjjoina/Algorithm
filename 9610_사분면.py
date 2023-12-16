import sys; input = sys.stdin.readline

Q1 = Q2 = Q3 = Q4 = AXIS = 0

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    
    if x == 0 or y == 0:
        AXIS += 1
    elif x > 0:
        if y > 0 :
            Q1 += 1
        else:
            Q4 += 1
    else:
        if y > 0:
            Q2 += 1
        else:
            Q3 += 1

print('Q1:', Q1)
print('Q2:', Q2)
print('Q3:', Q3)
print('Q4:', Q4)
print('AXIS:', AXIS)