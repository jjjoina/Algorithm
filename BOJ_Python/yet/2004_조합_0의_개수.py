import sys; input = sys.stdin.readline

def count5(x):
    '''
    x!를 소인수분해 했을 때 5의 지수를 반환하는 함수
    '''
    rst = 0
    d = 5
    while True:
        q = x // d
        if q == 0:
            break
        rst += q
        d *= 5

    return rst

for i in range(200):
    print(i, count5(i))

# n, m = map(int, input().split())
# print(count5(n) - count5(m) - count5(n-m))