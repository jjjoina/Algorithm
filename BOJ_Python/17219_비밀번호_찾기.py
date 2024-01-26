import sys; input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for _ in range(N):
    url, pw = input().rstrip().split()
    dic[url] = pw
for _ in range(M):
    print(dic[input().rstrip()])