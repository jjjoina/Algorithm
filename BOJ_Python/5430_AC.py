import sys; input = sys.stdin.readline
from collections import deque

def AC(lst):
    for f in p:
        if f == 'R':
            # 배열 뒤집기
            lst = deque(list(lst)[::-1])
        else:
            if lst:
                # 첫 번째 수 버리기
                lst.popleft()
            else:
                return 'error'
    
    return list(lst)


T = int(input())
for _ in range(T):
    p = input().strip() # 함수
    n = int(input())
    lst = input().strip().strip('[]')
    if lst:
        lst = deque(map(int, lst.split(',')))
    else:   # 현재 lst = []
        lst = deque()

    print(AC(lst))