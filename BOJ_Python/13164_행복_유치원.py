import sys; input = sys.stdin.readline

N, K = map(int, input().split())
heights = list(map(int, input().split()))

diff_list = [heights[i+1] - heights[i] for i in range(N-1)]
diff_list.sort()
ans = sum(diff_list[:N-K]) if diff_list else 0

print(ans)