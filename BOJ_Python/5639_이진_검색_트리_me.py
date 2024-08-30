# 풀이 1. [Pypy3 243640KB, 1640ms] 트리 정보를 구성한 후 후위 순회
# 입력이 전위 순회로 주어진다는 것을 활용하지 않았다.
import sys; input = sys.stdin.readline
sys.setrecursionlimit(20000)

def push(new_v, cur_v):
    if new_v < cur_v:
        if tree[cur_v][0] == -1:
            tree[cur_v][0] = new_v
            tree[new_v] = [-1, -1]
        else:
            push(new_v, tree[cur_v][0])
    else:
        if tree[cur_v][1] == -1:
            tree[cur_v][1] = new_v
            tree[new_v] = [-1, -1]
        else:
            push(new_v, tree[cur_v][1])


def postorder_traversal(v):
    if v == -1:
        return

    postorder_traversal(tree[v][0])
    postorder_traversal(tree[v][1])
    ans.append(str(v))


tree = {}
root = int(input())
tree[root] = [-1, -1]
ans = []

while True:
    try:
        new_v = int(input())
        push(new_v, root)
    except:
        postorder_traversal(root)
        print('\n'.join(ans))
        break