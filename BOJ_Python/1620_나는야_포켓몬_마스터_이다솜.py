import sys; input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}
for i in range(1, N+1):
    pokemon = input().rstrip()
    dic[pokemon] = i
    dic[str(i)] = pokemon

for _ in range(M):
    print(dic[input().rstrip()])