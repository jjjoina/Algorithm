import sys; input = sys.stdin.readline

for _ in range(int(input())):
    V, E = map(int, input().split())
    print(2 - V + E)