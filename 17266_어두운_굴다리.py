import sys; input = sys.stdin.readline

N = int(input())
M = int(input())
lst = list(map(int, input().split()))

# 가로등의 간격 리스트
# 첫 번째 가로등의 왼쪽과 마지막 가로등의 오른쪽은 값을 두 배로 한다.
# why? 한 방향에서만 비추므로 그만큼 가로등이 높이 올라가야 한다.
intervals = [2*lst[0]]
for i in range(1, M):
    intervals.append(lst[i] - lst[i-1])
intervals.append(2*(N-lst[M-1]))

# 최대 간격을 반으로 나눠서 올림한 값이 정답!
ans = max(intervals) / 2
if ans == int(ans): ans = int(ans)
else: ans = int(ans) + 1
print(ans)