# 풀이 2. [Pypy3 143356KB, 212ms] [Python 3 33468KB, 2404ms]
# 각 서브트리에서 V, L, R 범위를 확인하고 검사
# 입력이 전위 순회로 주어진다는 것을 활용
import sys; input = sys.stdin.readline
sys.setrecursionlimit(20000)

def preorder_to_postorder(start, end):
    if start > end:
        return

    if start == end:
        print(preorder[start])
        return

    # 오른쪽 서브 트리의 시작 인덱스 찾기
    r = start + 1
    while r <= end and preorder[r] < preorder[start]:
        r += 1

    preorder_to_postorder(start + 1, r - 1)
    preorder_to_postorder(r, end)
    preorder_to_postorder(start, start)


preorder = []

while True:
    try:
        preorder.append(int(input()))
    except:
        preorder_to_postorder(0, len(preorder) - 1)
        break