import sys; input = sys.stdin.readline

n = int(input())

stack = [0]     # 땅을 넣고 시작. 땅은 pop 될일 없다.
ans = 0

for _ in range(n):
    x, h = map(int, input().split())
    
    # 더 낮은 건물을 만난 경우 그 건물 초과 높이의 건물은 끝났다는 의미.
    # 해당 건물들을 pop
    while stack[-1] > h:
        stack.pop()

    # 높이가 같은 경우 해당 건물은 이미 카운트했으므로(=구면이므로) 패스
    if stack[-1] == h:
        continue

    # 더 높은 건물(=초면인 건물)인 경우이므로 push하며 카운트
    stack.append(h)
    ans += 1

print(ans)