import sys; input = sys.stdin.readline
from collections import deque

def input_tree():
    tree = [[-1, []] for _ in range(N + 1)]

    for _ in range(N - 1):
        parent, child = map(int, input().split())
        tree[parent][1].append(child)
        tree[child][0] = parent

    return tree


def find_root():
    for i in range(1, N + 1):
        if tree[i][0] == -1:
            return i


def fill_depth():
    q = deque()
    depth = [-1] * (N + 1)
    q.append(root)
    depth[root] = 0

    while q:
        v = q.popleft()
        for w in tree[v][1]:
            q.append(w)
            depth[w] = depth[v] + 1

    return depth


def find_nearest_common_ancestor():
    v1, v2 = map(int, input().split())

    while depth[v1] < depth[v2]:
        v2 = tree[v2][0]

    while depth[v1] > depth[v2]:
        v1 = tree[v1][0]

    while v1 != v2:
        v1 = tree[v1][0]
        v2 = tree[v2][0]

    return v1


T = int(input())
for _ in range(T):
    N = int(input())

    tree = input_tree()

    root = find_root()

    depth = fill_depth()

    print(find_nearest_common_ancestor())