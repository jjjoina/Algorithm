import sys; input = sys.stdin.readline

def preorder(v):
    # 이 함수를 호출한 노드가 잎이었다면 돌려보냄
    if v == '.': return

    # 본인 출력
    print(v, end='')
    # 왼쪽 자식 탐색
    preorder(tree[v][0])
    # 오른쪽 자식 탐색
    preorder(tree[v][1])


def inorder(v):
    # 이 함수를 호출한 노드가 잎이었다면 돌려보냄
    if v == '.': return

    # 왼쪽 자식 탐색
    inorder(tree[v][0])
    # 본인 출력
    print(v, end='')
    # 오른쪽 자식 탐색
    inorder(tree[v][1])


def postorder(v):
    # 이 함수를 호출한 노드가 잎이었다면 돌려보냄
    if v == '.': return

    # 왼쪽 자식 탐색
    postorder(tree[v][0])
    # 오른쪽 자식 탐색
    postorder(tree[v][1])
    # 본인 출력
    print(v, end='')


N = int(input())

tree = {}
for _ in range(N):
    v, l, r = input().split()
    tree[v] = [l, r]

preorder('A')
print()
inorder('A')
print()
postorder('A')