import sys; input = sys.stdin.readline

while True:
    edges = list(map(int, input().split()))
    if sum(edges) == 0: break

    if max(edges) >= sum(edges) - max(edges):
        print('Invalid')
    elif edges[0] == edges[1] and edges[0] == edges[2]:
        print('Equilateral')
    elif edges[0] == edges[1] or edges[0] == edges[2] or edges[1] == edges[2]:
        print('Isosceles')
    else:
        print('Scalene')