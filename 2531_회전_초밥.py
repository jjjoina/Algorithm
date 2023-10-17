import sys; input = sys.stdin.readline

N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]

dic = {}
ans = 0
# 모든 경우의 수를 조사
for i in range(N):
    if i >= k:
        dic[belt[i-k]] -= 1
        if dic[belt[i-k]] == 0:
            dic.pop(belt[i-k])

    dic[belt[i]] = dic.get(belt[i], 0) + 1
    
    rst = len(dic)
    if c not in dic: rst += 1
    ans = max(ans, rst)

print(ans)