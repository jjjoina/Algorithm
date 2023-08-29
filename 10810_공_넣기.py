# i~j번 바구니에 k번 공 넣음
# 바구니에 이미 공이 있으면 빼고 넣음

N, M = map(int, input().split())
baskets = [0] * (N+1)
for _ in range(M):
    i, j, k = map(int, input().split())
    baskets[i:j+1] = [k] * (j-i+1)
print(*baskets[1:])