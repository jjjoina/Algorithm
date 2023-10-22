import sys; input = sys.stdin.readline

def solve():
    t = []
    for i in range(N-1, 0, -1):
        t.append(lst.pop())

        if t[-1] > lst[i-1]:
            for j in range(len(t)):
                if t[j] > lst[i-1]:
                    t[j], lst[i-1] = lst[i-1], t[j]
                    return lst + t
    
    return [-1]


N = int(input())
lst = list(map(int, input().split()))

print(*solve())