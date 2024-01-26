import sys; input = sys.stdin.readline

N = int(input())
heights = [0] + list(map(int, input().split()))

num = [0] * (N+1)
close = [0] * (N+1)

# 좌 -> 우 순회
stack = []
cnt = 0     # stack의 길이
for i in range(1, N+1):
    # 본인 이하의 건물 모두 pop
    while stack and heights[i] >= stack[-1][1]:
        stack.pop()
        cnt -= 1
    
    # num과 close에 정보 저장
    num[i] += cnt
    if stack:   # 보이는 건물이 있는 경우
        close[i] = stack[-1][0] # 왼쪽에 있는 건물 중 가장 가까운 건물 번호 대입
    
    # 본인 push
    stack.append((i, heights[i]))
    cnt += 1

# 우 -> 좌 순회
stack = []
cnt = 0     # stack의 길이
for i in range(N, 0, -1):
    # 본인 이하의 건물 모두 pop
    while stack and heights[i] >= stack[-1][1]:
        stack.pop()
        cnt -= 1
    
    # num과 close에 정보 저장
    num[i] += cnt
    if stack:   # 보이는 건물이 있는 경우
        if close[i] == 0:   # 좌 -> 우에서 저장된 게 없는 경우
            close[i] = stack[-1][0]
        else:
            # 신규가 더 가까운 경우에만 갱신
            if stack[-1][0] - i < i - close[i]:
                close[i] = stack[-1][0]
    
    # 본인 push
    stack.append((i, heights[i]))
    cnt += 1

for i in range(1, N+1):
    if num[i]:
        print(num[i], close[i])
    else:
        print(num[i])