import sys; input = sys.stdin.readline

edges = list(map(int, input().split()))
edges.sort()
if edges[2] >= edges[0] + edges[1]:
    edges[2] = edges[0] + edges[1] - 1
print(sum(edges))