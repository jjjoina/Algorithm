import sys; input = sys.stdin.readline

N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0]
ans = 0
for i in range(N-1):
    # i번째 주유소의 가격이 min_price보다 더 싼 경우 갱신
    if prices[i] < min_price:
        min_price = prices[i]
    
    ans += min_price * distances[i]

print(ans)